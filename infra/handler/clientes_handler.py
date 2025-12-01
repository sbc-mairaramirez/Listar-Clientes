#entrypoint de la API para exponer endpoints HTTP
#handler -> expone un metodo para FastAPI (adaptador de entreda)
from fastapi import APIRouter, HTTPException
from application.listar_clientes_use_case import ListarClientesUseCase
from infra.repository.clientes_repository_pg import ClientesRepositoryPg
from infra.shared.logger import logger

#routeador que sera incluido en FastAPI
router = APIRouter()

@router.get("/clientes")
def listar_clientes_handler():
    """
    Handler de entrada para el endpoint GET /clientes.
    """
    try:
        repo = ClientesRepositoryPg()
        use_case = ListarClientesUseCase(repo)
        return use_case.ejecutar()
    except Exception as e:
        logger.error(f"Fallo en handler GET /clientes")
        raise HTTPException(status_code=500, detail= str(e))
