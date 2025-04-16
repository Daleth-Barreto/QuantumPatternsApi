from fastapi import APIRouter, Query
from fastapi.responses import Response
from app.services.quantum_generator import generate_pattern_image
from app.models.request_models import PatternRequest

router = APIRouter()

@router.post("/generate")
def generate_pattern(data: PatternRequest):
    image = generate_pattern_image(data)
    return Response(content=image, media_type="image/png")
