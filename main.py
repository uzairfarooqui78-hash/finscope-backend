@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()
    df = pd.read_excel(BytesIO(contents), engine="openpyxl")

    return {
        "columns": df.columns.tolist(),
        "preview": df.head().to_dict()
    }
