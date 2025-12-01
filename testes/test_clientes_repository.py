# tests/test_clientes_repository.py
from infra.repository.clientes_repository_pg import ClientesRepositoryPg
from unittest.mock import MagicMock, patch
from domain.cliente import Cliente

def test_listar_clientes_repository():
    cursor_mock = MagicMock()
    cursor_mock.fetchall.return_value = [
        {
            "id": 1,
            "name": "Juan",
            "email": "juan@example.com",
            "created_at": "2024-01-01"
        }
    ]

    db_mock = MagicMock()
    db_mock.get_cursor.return_value = cursor_mock

    with patch("infra.repository.clientes_repository_pg.DatabaseConnection", return_value=db_mock):
        repo = ClientesRepositoryPg()
        clientes = repo.listar()

    assert len(clientes) == 1
    assert isinstance(clientes[0], Cliente)
    assert clientes[0].nombre == "Juan"
