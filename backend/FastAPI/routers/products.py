from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["Products"],
                   responses={404: {"message": "Not Found"}})


products_list = ["Apples", "Pears", "Strawberrys", "Grapes"]


@router.get('/', status_code=200)
async def get_products():
    return products_list

@router.get('/{id}', status_code=200)
async def get_product(id: int):
    return products_list[id]