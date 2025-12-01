# domain/cliente.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    fecha_creacion: datetime
