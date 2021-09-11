from src.storages.db_storage import MySQLDBStorage


def test_success(mocker, test_x4_entity) -> None:
    """Успешное сохранение сущности X4 в БД."""
    mocked_create_table = mocker.patch.object(
        MySQLDBStorage, "create_table_if_not_exist"
    )
    mocked_insert = mocker.patch.object(
        MySQLDBStorage, "insert_entity_to_table"
    )
    mysql_storage = MySQLDBStorage(db_connect=mocker.Mock())

    mysql_storage.save(test_x4_entity)  # act

    mocked_create_table.assert_called_once()
    mocked_insert.assert_called_once()
