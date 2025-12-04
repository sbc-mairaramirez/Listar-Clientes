import pytest
from infra.repository.clientes_repository_pg import ClientesRepositoryPg
from infra.shared.exceptions import DatabaseQueryError

def test_listar_raises_database_query_error(monkeypatch):
    # Simula que DatabaseConnection lanza error
    def fake_init(self):
        raise Exception("DB failure")

    monkeypatch.setattr(
        "infra.repository.clientes_repository_pg.DatabaseConnection.__init__",
        fake_init
    )

    repo = ClientesRepositoryPg()

    with pytest.raises(DatabaseQueryError):
        repo.listar()
