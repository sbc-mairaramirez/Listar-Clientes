# tests/test_clientes_handler.py
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock
from domain.cliente import Cliente

client = TestClient(app)

def test_listar_clientes_handler():
    cliente_falso = Cliente(
        id=1,
        nombre="Juan",
        email="juan@example.com",
        fecha_creacion="2024-01-01"
    )

    # Creamos un mock para la instancia del repositorio
    repo_mock = MagicMock()
    repo_mock.listar.return_value = [cliente_falso]

    # Patch en la ruta donde el handler crea la clase (>> donde se importó la clase)
    with patch("infra.handler.clientes_handler.ClientesRepositoryPg", return_value=repo_mock):
        response = client.get("/clientes")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["nombre"] == "Juan"
