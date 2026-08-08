from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def greet():
    return {"message": "Welcome to SaheliOS"}

@router.get("/health")
def status():
    return{"message": "Healthy!!"}