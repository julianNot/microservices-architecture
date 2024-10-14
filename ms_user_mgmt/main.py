from fastapi import FastAPI
from app.routers.customer_routes import customer_router  # Importa el router de las rutas

# Instancia de la aplicación FastAPI
app = FastAPI()

# Incluye las rutas del customer_router
app.include_router(customer_router)