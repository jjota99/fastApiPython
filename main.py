from datetime import datetime

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

# rota raiz
@app.get("/")
def read_root():
    return {'hello': 'world'}

# rota horario
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@app.get("/horario")
def horario():
    return {"horario": current_time}

# criando model
class Analise(BaseModel):
    diabeticos: int
    hipertensos: int
    quadrimestre: str

# criando base de dados
dados_analise = [
    Analise(diabeticos=125, hipertensos=111, quadrimestre="Q1/2021"),
    Analise(diabeticos=91, hipertensos=73, quadrimestre="Q2/2021"),
    Analise(diabeticos=60, hipertensos=58, quadrimestre="Q3/2021"),
]

# rota simulando dados do gráfico no teste frontend
@app.get("/analytics")
def get_todas_analises():
    return dados_analise