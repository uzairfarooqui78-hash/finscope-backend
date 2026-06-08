from fastapi import FastAPI, UploadFile, File
import pandas as pd

from kpi_engine import calculate_kpis
from scoring_engine import run_scoring

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FinScope Backend Running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    df = pd.read_excel(file.file)

    kpis = calculate_kpis(df)
    result = run_scoring(kpis)

    return {
        "kpis": kpis,
        "result": result
    }

@app.post("/kpis")
async def get_kpis(file: UploadFile = File(...)):

    df = pd.read_excel(file.file)
    kpis = calculate_kpis(df)

    return {"kpis": kpis}

@app.post("/score")
async def score(file: UploadFile = File(...)):

    df = pd.read_excel(file.file)

    kpis = calculate_kpis(df)
    result = run_scoring(kpis)

    return {"result": result}
