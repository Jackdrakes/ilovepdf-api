from pydantic import BaseModel

class ConversionResponse(BaseModel):
    message: str
    file_urls: list[str] = None  # List of URLs for converted images or PDF file path.