#Caso de uso: Listar clientes
#responsable de orquestar la operacion de consultar al repositorio 
from domain.cliente_repository import ClienteRepositoryInterface

class ListarClientesUseCase:
    def __init__(self, repo: ClienteRepositoryInterface):
        #llama al repositorio(siguiendo la arquitectura hexagonal)
        self.repo = repo

    def ejecutar(self):
        #ejecuta la operacion delegando la carga al repositorio 
        return self.repo.listar()
