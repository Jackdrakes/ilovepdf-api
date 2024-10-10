import os

class Settings:
    IMAGE_DIR: str = os.getenv("IMAGE_DIR", "images")

settings = Settings()