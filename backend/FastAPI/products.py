from fastapi import FastAPI

app = FastAPI()

@app.get('/products', tags=["Products"], status_code=200)
def get_products():
    return ["Apples", "Pears", "Strawberrys", "Grapes"]