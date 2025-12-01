# main.py (opcional)
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from infra.handler.clientes_handler import router as clientes_router

app = FastAPI(title="Customer API", version="1.0.0")
app.include_router(clientes_router)


