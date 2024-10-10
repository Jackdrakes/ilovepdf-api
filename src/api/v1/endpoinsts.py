from fastapi import UploadFile, File, HTTPException
from src.services.pdf_conversions import convert_pdf_to_images # convert_image_to_pdf

async def convert_pdf_to_image(file: UploadFile = File(...)):
    try:
        return await convert_pdf_to_images(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# async def convert_image_to_pdf(file: UploadFile = File(...)):
#     try:
#         return await convert_image_to_pdf(file)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))