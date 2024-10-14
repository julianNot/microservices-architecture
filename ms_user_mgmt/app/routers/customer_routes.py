from fastapi import APIRouter, Depends
from app.controllers.customer_controller import create_customer, get_customer, delete_customer
from app.models import Customer
from app.utils.security import oauth2_scheme

# Instancia de APIRouter
customer_router = APIRouter()

# Ruta para crear un nuevo cliente
@customer_router.post("/customers/")
async def createcustomer(customer: Customer, token: str = Depends(oauth2_scheme)):
    return await create_customer(customer)

# Ruta para obtener un cliente por su documento
@customer_router.get("/customers/{document}")
async def findcustomerbyid(document: str, token: str = Depends(oauth2_scheme)):
    return await get_customer(document)

# Ruta para eliminar un cliente por su documento
@customer_router.delete("/customers/{document}")
async def deletecustomer(document: str, token: str = Depends(oauth2_scheme)):
    return await delete_customer(document)
