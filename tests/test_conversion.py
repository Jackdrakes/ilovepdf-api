import pytest

@pytest.mark.asyncio
async def test_convert_pdf_to_image(client):
    with open("test.pdf", "rb") as f:
        response = await client.post("/v1/convert/pdf2image/", files={"file": f})
    
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_convert_image_to_pdf(client):
    with open("test_image.png", "rb") as f:
        response = await client.post("/v1/convert/image2pdf/", files={"file": f})
    
    assert response.status_code == 200 