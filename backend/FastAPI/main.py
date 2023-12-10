from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import products, users
# import class so as to present static files, imgs.
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
# url: http://127.0.0.1:8000/static/imgs/name_of_the_file.jpeg
app.mount("/static", StaticFiles(directory="static"), name="img")


@app.get('/', tags=["Root"])
async def root():
    return JSONResponse(content={"sample text": "Holi JSON sample text en root"})

@app.get('/url', tags=["URL"])
async def url():
    return {"url": "https://www.google.com"}