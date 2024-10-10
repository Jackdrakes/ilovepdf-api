from fastapi import APIRouter
from src.api.v1.endpoinsts import convert_pdf_to_image # convert_image_to_pdf

router = APIRouter()

router.post("/convert/pdf2image/", response_model=dict)(convert_pdf_to_image)
# router.post("/convert/image2pdf/", response_model=dict)(convert_image_to_pdf)