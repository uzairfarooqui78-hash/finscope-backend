from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        contents = await file.read()

        df = pd.read_excel(
            BytesIO(contents),
            engine="openpyxl"
        )

        return {
            "status": "ok",
            "columns": df.columns.tolist(),
            "rows": len(df)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
