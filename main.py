@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_excel(contents, engine="openpyxl")

    kpis = calculate_kpis(df)
    result = run_scoring(kpis)

    return {
        "kpis": kpis,
        "result": result
    }
