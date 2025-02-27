from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db_connection

app = FastAPI()

# Modelo para recibir los datos correctamente
class LoginRequest(BaseModel):
    usuario: str
    contraseña: str

@app.get("/usuarios")
async def get_users():
    """ Obtiene todos los usuarios con sus datos en formato JSON """
    conn = get_db_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM inicio2")  
                users = cursor.fetchall()
                return {"usuarios": users}
             
    except Exception as ex:
        return {"error": str(ex)}

@app.post("/login")
async def login(user_data: LoginRequest):
    """ Valida si el usuario y contraseña existen en la BD """
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    usuario = user_data.usuario
    contraseña = user_data.contraseña

    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM inicio2 WHERE usuario = %s AND contraseña = %s", (usuario, contraseña))
            user = cursor.fetchone()

    # Corrección en la validación
    if user:  # Si encontró un usuario, es exitoso
        return {"message": "Login exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
