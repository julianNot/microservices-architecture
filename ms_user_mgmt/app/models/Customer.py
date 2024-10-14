from pydantic import BaseModel

# Modelo Pydantic para los datos del cliente
class Customer(BaseModel):
    document: str
    firstname: str
    lastname: str
    address: str
    phone: str
    email: str  # Valida que el email sea correcto