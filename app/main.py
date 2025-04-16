from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import patterns

app = FastAPI(title="Quantum Pattern API")

# Configurar CORS
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "https://daleth-barreto.github.io/QuantumPatternsApi/",
    "https://quantumpatternsapi.onrender.com", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas de patrones
app.include_router(patterns.router, prefix="/patterns", tags=["Quantum Patterns"])
