from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/', tags=["Root"])
async def root():
    return JSONResponse(content={"sample text": "Holi JSON sample text en root"})

@app.get('/url', tags=["URL"])
async def url():
    return {"url": "https://www.google.com"}