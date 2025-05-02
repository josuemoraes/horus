from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 📦 Pega a variável de ambiente DATABASE_URL (Render já tem configurado)
DATABASE_URL = os.getenv("DATABASE_URL")

# ⚙️ Cria o engine e sessão de banco
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔨 Base para os modelos
Base = declarative_base()

# 🔁 Função que o FastAPI usa para injetar o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
