import os
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Clave secreta para firmar y verificar el token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"  # Algoritmo de firma (puedes cambiarlo si lo deseas)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para verificar el token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Retorna los datos del payload si es válido
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
