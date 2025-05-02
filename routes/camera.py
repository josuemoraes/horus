from fastapi import APIRouter

router = APIRouter()

@router.post("/detect")
def detect():
    return {"message": "Detect funcionando"}
