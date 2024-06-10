from fastapi import FastAPI, Response, status
from pydantic import BaseModel

from enum import Enum
from json import dumps, loads

app = FastAPI(summary="""API di test per il corso di python""", version="0.0.1")

class VeicoloData(BaseModel):
    id: int | None = None
    tipo: str | None = None
    nome: str | None = None
    marca: str | None = None
    modello: str | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

VEICOLI = [
    {
        "id": 0,
        "tipo": "automobile",
        "nome": "mia_macchina",
        "marca": "opel",
        "modello": "astra"
    },
    {
        "id": 1,
        "tipo": "bicicletta",
        "nome": "city_bike",
        "marca": "bianchi",
        "modello": "spillo"
    }
]
## Commentata per mostrare il funzionamento della più
## generica lista_filtrata allo stesso endpoint
# @app.get("/veicoli")
# async def lista_veicoli():
#     """ritorna la lista di veicoli"""
#     return VEICOLI


@app.get("/veicoli")
async def lista_filtrata(tipo: str = None):
    if tipo:
        return [ v for v in VEICOLI if v["tipo"] == tipo ]
    else:
        return VEICOLI
        
        


@app.get("/veicoli/automobili")
async def lista_auto():
    return [v for v in VEICOLI if v["tipo"] == "automobile"]



@app.get("/veicoli/{veicolo_id}", status_code=200)
async def veicolo_id(veicolo_id: int):
    result = {}

    for v in VEICOLI:
        if v["id"] == veicolo_id:
            result = v
            break

    return result

@app.get("/veicoli/{tipo}", status_code=200)
async def lista_per_tipo(tipo: str):
    result = []
    for v in VEICOLI:
        if v["tipo"] != tipo:
            continue
        else:
            result.append(v)
            break

    return result

@app.get("/veicoli/", status_code=200)
async def lista_per_tipo(tipo: str):
    result = []
    for v in VEICOLI:
        if v["tipo"] != tipo:
            continue
        else:
            result.append(v)
            break

    return result

@app.post("/veicoli/insert", status_code=201)
async def insert_veicolo(nuovo: VeicoloData):
    VEICOLI.append(nuovo)
    return nuovo

@app.put("/veicoli/update/{veicolo_id}", status=status.HTTP_202_ACCEPTED)
async def aggiorna_viecolo(veicolo_id: int, veicolo: VeicoloData):
    pass