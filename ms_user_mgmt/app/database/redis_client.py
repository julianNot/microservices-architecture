import redis

# Configuramos el cliente de Redis
r = redis.Redis(
    host='localhost',  # O la IP donde esté Redis
    port=6379,         # Puerto por defecto de Redis
    db=0               # Base de datos que usará (por defecto es la 0)
)
