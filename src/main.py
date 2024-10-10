from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.router import router as api_router

app = FastAPI()

origins =[
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"], # ["*"]
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
    expose_headers=["Content-Disposition"],  # Expose the Content-Disposition header

)



app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF/Image Converter API"}