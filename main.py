from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo entrada
class RecomendacionRequest(BaseModel):
    ia: str
    edad: int
    genero: str
    ocasion: str
    presupuesto: float
    gustos: List[str]

# Cargar catálogo una sola vez al inicio
with open("catalogo_regalidea.json", encoding="utf-8") as f:
    productos = json.load(f)

@app.post("/recomendar")
async def recomendar(req: RecomendacionRequest):
    max_presupuesto = req.presupuesto + 10  # tolerancia
    coincidencias = []

    tags_usuario = [req.genero.lower(), req.ocasion.lower()] + [g.lower() for g in req.gustos]

    for prod in productos:
        if prod["precio"] <= max_presupuesto:
            score = sum(1 for tag in prod["tags"] if tag.lower() in tags_usuario)
            coincidencias.append((score, prod))

    coincidencias.sort(reverse=True, key=lambda x: x[0])
    recomendaciones = [item[1] for item in coincidencias if item[0] > 0][:20]

    if req.ia.upper() == "DEA":
        mensaje_final = "🌟 Gracias por confiar en regalidea.es. Recuerda, el mejor regalo es el que emociona desde el primer instante. ¿Quieres otra idea?"
    else:
        mensaje_final = "🔎 Gracias por visitar regalidea.es. Aquí tienes las mejores opciones según lógica y presupuesto."

    return {
        "ia": req.ia,
        "recomendaciones": recomendaciones,
        "mensaje_final": mensaje_final
    }
