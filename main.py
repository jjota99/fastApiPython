from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


@app.get("/")
def read_root():
    return 'Horario atual: %s' % current_time
