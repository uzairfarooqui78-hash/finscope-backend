from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

from kpi_engine import calculate_kpis
from scoring_engine import run_scoring

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "live",
        "product": "FinScope KPI Engine",
        "version": "1.0"
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()
    df = pd.read_excel(BytesIO(contents), engine="openpyxl")

    # STEP 1: KPIs
    kpis = calculate_kpis(df)

    # STEP 2: SCORE
    result = run_scoring(kpis)

    # STEP 3: FINAL PRODUCT RESPONSE
    return {
        "status": "success",
        "summary": {
            "total_rows": len(df),
            "columns": df.columns.tolist()
        },
        "kpis": kpis,
        "score": result,
        "insight": "Company health analysis completed"
    }
