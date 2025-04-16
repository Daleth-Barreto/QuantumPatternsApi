from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import patterns

# Crear la aplicación FastAPI
app = FastAPI(title="Quantum Pattern API")

# Configurar CORS
origins = [
    "http://localhost",  # Permite solicitudes desde localhost
    "http://127.0.0.1",  # Permite solicitudes desde localhost usando 127.0.0.1
    "*",  # Permite solicitudes desde cualquier origen (esto puedes restringirlo más)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir cualquier método (GET, POST, etc.)
    allow_headers=["*"],  # Permitir cualquier cabecera
)

# Incluir las rutas de patrones
app.include_router(patterns.router, prefix="/patterns", tags=["Quantum Patterns"])
