from fastapi import APIRouter


lista_productos = ["producto1, producto2, producto3, producto4", "producto 5"]

products = APIRouter(prefix="/products",
                   tags=["products"])

@products.get("/")
async def productos():
    return lista_productos

