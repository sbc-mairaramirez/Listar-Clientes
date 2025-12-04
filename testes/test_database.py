import os
from unittest.mock import patch, MagicMock
from infra.config.database import DatabaseConnection


@patch("psycopg2.connect")
def test_database_connection_without_ssl(mock_connect):
    """Prueba conexión sin sslmode en variables de entorno."""
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    with patch.dict(os.environ, {
        "DB_NAME": "testdb",
        "DB_USER": "testuser",
        "DB_PASS": "123",
        "DB_HOST": "localhost",
        "DB_PORT": "5432"
    }):
        db = DatabaseConnection()

        # verificar que se llamó a la conexión
        mock_connect.assert_called_once()
        args = mock_connect.call_args.kwargs

        assert args["dbname"] == "testdb"
        assert args["user"] == "testuser"
        assert args["password"] == "123"
        assert args["host"] == "localhost"
        assert args["port"] == "5432"

        assert db.connection.autocommit is True


@patch("psycopg2.connect")
def test_database_connection_with_ssl(mock_connect):
    """Prueba conexión cuando sslmode está definido."""
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    with patch.dict(os.environ, {
        "DB_NAME": "testdb",
        "DB_USER": "testuser",
        "DB_PASS": "123",
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_SSLMODE": "require"
    }):
        DatabaseConnection()

        # verificar que la llamada incluye sslmode
        args = mock_connect.call_args.kwargs
        assert args["sslmode"] == "require"


@patch("psycopg2.connect")
def test_get_cursor(mock_connect):
    """Prueba que get_cursor llama correctamente al cursor."""
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    db = DatabaseConnection()
    cursor = db.get_cursor()

    assert cursor == mock_cursor
    mock_conn.cursor.assert_called_once()
