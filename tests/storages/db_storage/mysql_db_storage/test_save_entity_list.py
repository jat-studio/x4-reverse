from src.storages.db_storage import MySQLDBStorage


def test_success(mocker, test_x4_entity, test_mysql_storage) -> None:
    """Успешное сохранение списка сущностей вселенной X4 в БД."""
    mocked_create_table = mocker.patch.object(
        MySQLDBStorage, "create_table_if_not_exist"
    )
    mocked_insert = mocker.patch.object(
        MySQLDBStorage, "insert_entity_list_to_tables"
    )

    test_mysql_storage.save_entity_list([test_x4_entity])  # act

    mocked_create_table.assert_called_once()
    mocked_insert.assert_called_once()
