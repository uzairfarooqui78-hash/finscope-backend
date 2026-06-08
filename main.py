from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

from kpi_engine import calculate_kpis
from scoring_engine import run_scoring

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FinScope Backend Running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_excel(BytesIO(contents), engine="openpyxl")

    kpis = calculate_kpis(df)
    result = run_scoring(kpis)

    return {
        "kpis": kpis,
        "result": result
    }
