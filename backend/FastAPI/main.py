from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)


@app.get('/', tags=["Root"])
async def root():
    return JSONResponse(content={"sample text": "Holi JSON sample text en root"})

@app.get('/url', tags=["URL"])
async def url():
    return {"url": "https://www.google.com"}