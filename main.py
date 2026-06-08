from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        contents = await file.read()

        if not contents:
            return {"error": "Empty file uploaded"}

        df = pd.read_excel(BytesIO(contents), engine="openpyxl")

        return {
            "status": "success",
            "columns": df.columns.tolist(),
            "rows": len(df),
            "preview": df.head(3).to_dict()
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
