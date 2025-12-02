from infra.config.database import DatabaseConnection
from domain.cliente import Cliente
from domain.cliente_repository import ClienteRepositoryInterface
from infra.shared.logger import logger
from infra.shared.exceptions import DatabaseQueryError   # <-- Import de la excepción específica


class ClientesRepositoryPg(ClienteRepositoryInterface):

    def listar(self):
        """
        Obtiene todos los clientes desde Postgres.
        Implementa la interfaz definida para el dominio.
        """
        try:
            db = DatabaseConnection()
            cursor = db.get_cursor()

            cursor.execute("SELECT * FROM customers ORDER BY id;")
            rows = cursor.fetchall()

            clientes = [
                Cliente(
                    id=row["id"],
                    nombre=row["name"],
                    email=row["email"],
                    fecha_creacion=row["created_at"]
                )
                for row in rows
            ]

            logger.info("Clientes obtenidos exitosamente desde Postgres.")
            return clientes

        except Exception as e:
            logger.error("Error consultando Postgres: %s", e)   # <-- Sin f-string
            raise DatabaseQueryError(
                "No fue posible obtener los clientes desde la base de datos."
            ) from e   # <-- Excepción específica con causa
