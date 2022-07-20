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
    return {current_time}

