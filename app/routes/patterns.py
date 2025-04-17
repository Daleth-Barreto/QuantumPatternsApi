from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO
from app.services.quantum_generator import generate_pattern_image
from app.models.request_models import PatternRequest

router = APIRouter()
from fastapi import Response

@router.options("/generate")
def options_handler():
    return Response(status_code=200)

@router.post("/generate")
def generate_pattern(data: PatternRequest):
    image_data = generate_pattern_image(data)
    
    return StreamingResponse(
        BytesIO(image_data),
        media_type="image/png",
        headers={"Content-Disposition": "inline; filename=quantum_pattern.png"}
    )

