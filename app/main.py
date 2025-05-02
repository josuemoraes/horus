import base64
import io
import time
from datetime import datetime
from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import face_recognition

from app.database import SessionLocal
from app.models import Deteccao

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de faces ativas na memória (temporário)
face_db = []
next_id = 1
EMBEDDING_TTL = 60
SIMILARIDADE_TOLERANCIA = 0.68

def ler_imagem(file: UploadFile) -> np.ndarray:
    image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
    return np.array(image)

@app.post("/camera/detect")
async def detectar_rosto(
    camera_id: str = Form(...),
    file: UploadFile = File(...)
):
    global next_id, face_db

    frame = ler_imagem(file)
    rgb_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, locations)
    now = time.time()
    novos_ids = []

    for encoding in encodings:
        match = False
        for pessoa in face_db:
            distance = np.linalg.norm(pessoa["encoding"] - encoding)
            if distance < SIMILARIDADE_TOLERANCIA:
                pessoa["last_seen"] = now
                pessoa["tempo"] += 1
                novos_ids.append(pessoa["id"])
                match = True
                break

        if not match:
            pessoa = {
                "id": next_id,
                "encoding": encoding,
                "inicio": now,
                "last_seen": now,
                "tempo": 1
            }
            face_db.append(pessoa)
            novos_ids.append(next_id)
            next_id += 1

    # Remover inativos e salvar no banco
    session = SessionLocal()
    ativos = []
    for pessoa in face_db:
        if now - pessoa["last_seen"] > EMBEDDING_TTL:
            dt_entrada = datetime.fromtimestamp(pessoa["inicio"])
            dt_saida = datetime.fromtimestamp(pessoa["last_seen"])
            tempo_total = int(pessoa["last_seen"] - pessoa["inicio"])

            registro = Deteccao(
                camera_id=camera_id,
                face_id=f"face{pessoa['id']}",
                duracao=tempo_total,
                horario=dt_saida
            )
            session.add(registro)
        else:
            ativos.append(pessoa)

    face_db = ativos
    session.commit()
    session.close()

    return JSONResponse(content={"message": "Detect registrado com sucesso", "faces": novos_ids})

@app.get("/")
def root():
    return {"message": "Horus API - OK"}
