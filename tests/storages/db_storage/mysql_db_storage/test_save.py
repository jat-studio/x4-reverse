from src.storages.db_storage import MySQLDBStorage
from src.x4_universe.entity import X4Entity


def test_success(mocker) -> None:
    """Успешное сохранение сущности X4 в БД."""
    mocked_create_table = mocker.patch.object(
        MySQLDBStorage, "create_table_if_not_exist"
    )
    mocked_insert = mocker.patch.object(
        MySQLDBStorage, "insert_entity_to_table"
    )

    MySQLDBStorage().save(  # act
        X4Entity(entity_type="test-type", entity_code="AVS-122")
    )

    mocked_create_table.assert_called_once()
    mocked_insert.assert_called_once()
