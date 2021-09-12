import pytest

from src.storages.db_storage import MySQLDBStorage


TEST_CREATE_TABLE_SQL_COMMAND = (
    "CREATE TABLE `test_type` ( "
    "`id` int NOT NULL AUTO_INCREMENT, "
    "`code` varchar(8) NOT NULL, "
    "PRIMARY KEY (`id`), "
    "UNIQUE KEY `code` (`code`) "
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"
)


def test_success_wo_create(mocked_db, test_x4_entity) -> None:
    """Создание таблицы в БД не должно запускаться, если таблица уже есть."""
    mocked_db_connect, mocked_db_cursor = mocked_db
    mysql_storage = MySQLDBStorage(db_connect=mocked_db_connect)
    mysql_storage._tables_list = [test_x4_entity.entity_type]

    mysql_storage.create_table_if_not_exist(test_x4_entity)  # act

    assert mysql_storage._tables_list == [test_x4_entity.entity_type]
    mocked_db_cursor.execute.assert_not_called()


@pytest.mark.parametrize(
    "before_tables_list,  after_tables_list",
    (
        ([], ["test_type"]),
        (["other_table"], ["other_table", "test_type"]),
    ),
    ids=("w_empty_db", "w_other_table_exist"),
)
def test_success(
    mocker, mocked_db, test_x4_entity, before_tables_list, after_tables_list
) -> None:
    """Создание таблицы в БД."""
    mocked_db_connect, mocked_db_cursor = mocked_db
    mysql_storage = MySQLDBStorage(db_connect=mocked_db_connect)
    mysql_storage._tables_list = before_tables_list
    mocker.patch.object(
        MySQLDBStorage, "gen_entity_specific_mysql_fields", return_value=""
    )

    mysql_storage.create_table_if_not_exist(test_x4_entity)  # act

    assert mysql_storage._tables_list == after_tables_list
    mocked_db_cursor.execute.assert_called_once_with(TEST_CREATE_TABLE_SQL_COMMAND)
