import os, shutil, time
import uuid, zipfile
from fastapi import BackgroundTasks
from fastapi.responses import FileResponse
from pdf2image import convert_from_bytes
from PIL import Image


BASE_DIR = "temp_files"


async def convert_pdf_to_images(file):

    # create unique folder for handling each pdf
    pdf_name = file.filename.rsplit('.', 1)[0]
    unique_folder = f'{pdf_name}_{uuid.uuid4().hex}'
    unique_folder_path = os.path.join(BASE_DIR, unique_folder)
    os.makedirs(unique_folder_path, exist_ok=True)
    
    zip_filename = f"{unique_folder}.zip"
    zip_path = os.path.join(BASE_DIR, zip_filename)

    try:
        # Read and convert pdf to images
        pdf_bytes = await file.read()
        images = convert_from_bytes(pdf_bytes)


        # save images in folder
        i= 1
        for image in images:
            image_name = f"page_{i}.png"
            image_path = os.path.join(unique_folder_path, image_name)
            image.save(image_path, "PNG")
            i+=1

        # Create a zip file
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, _, files in os.walk(unique_folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), 
                               os.path.relpath(os.path.join(root, file), unique_folder_path))

        def cleanup():
            # Clean up: remove the temporary folder and zip file
            os.remove(zip_path)

        return FileResponse(zip_path, media_type='application/zip', headers={'Content-Disposition': f"attachment; filename=\"{pdf_name}.zip\""}, background=BackgroundTasks(tasks=[cleanup])) # filename=f"{pdf_name}.zip"

    finally:
        # Clean up: remove the temporary folder and zip file
        shutil.rmtree(unique_folder_path, ignore_errors=True)
   


# async def convert_image_to_pdf(file):
#     image = Image.open(await file.read())
#     pdf_name = f"{uuid.uuid4()}.pdf"
#     pdf_full_path = os.path.join(BASE_DIR, pdf_name)

#     image.save(pdf_full_path, "PDF", resolution=100.0)

#     return {
#         "message": "Image converted to PDF successfully",
#         "file_url": pdf_full_path,
#     }