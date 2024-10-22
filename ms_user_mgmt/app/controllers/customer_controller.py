from fastapi import HTTPException
from app.models import Customer
from app.database.redis_client import r  # Importar el cliente Redis configurado

# Función para generar una clave única en Redis
def generate_customer_key(document: str) -> str:
    return f"customer:{document}"


async def create_customer(customer: Customer):
    key = generate_customer_key(customer.document)
    
    # Verificar si el cliente ya existe
    if r.exists(key):
        raise HTTPException(status_code=400, detail="Customer already exists")

    # Guardar los datos en Redis como un hash
    r.hmset(key, customer.dict())
    return {"message": "Customer created successfully"}


async def get_customer(document: str):
    key = generate_customer_key(document)

    # Verificar si el cliente existe
    if not r.exists(key):
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Obtener los datos del cliente
    customer_data = r.hgetall(key)
    return customer_data

async def delete_customer(document: str):
    key = generate_customer_key(document)

    # Verificar si el cliente existe
    if not r.exists(key):
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Eliminar el cliente
    r.delete(key)
    return {"message": "Customer deleted successfully"}


async def get_all_customers():
    # Obtener todas las claves que coincidan con el patrón "customer:*"
    all_keys = r.keys("customer:*")
    
    # Lista para almacenar todos los clientes
    customers = []
    
    # Obtener los datos de cada cliente
    for key in all_keys:
        customer_data = r.hgetall(key)
        if customer_data:  # Verificar que el cliente existe
            customers.append(customer_data)
    
    return customers
