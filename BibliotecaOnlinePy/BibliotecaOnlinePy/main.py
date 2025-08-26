from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.publicacoes import router as publicacoes_router

app = FastAPI(title="Biblioteca Online API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(publicacoes_router, prefix="/api/publicacoes")

@app.get("/")
def root():
    return {"message": "Biblioteca Online API - FastAPI"}
