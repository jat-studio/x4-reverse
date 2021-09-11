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
    mocked_db_cursor.fetchall.return_value = [test_x4_entity.entity_type]
    mysql_storage = MySQLDBStorage(db_connect=mocked_db_connect)

    mysql_storage.create_table_if_not_exist(test_x4_entity)  # act

    mocked_db_cursor.fetchall.assert_called_once()
    mocked_db_cursor.execute.assert_called_once()


@pytest.mark.parametrize(
    "fetchall_return",
    ([], ["other_table"]),
    ids=("w_empty_db", "w_other_table_exist"),
)
def test_success(mocker, mocked_db, test_x4_entity, fetchall_return) -> None:
    """Создание таблицы в БД."""
    mocked_db_connect, mocked_db_cursor = mocked_db
    mocked_db_cursor.fetchall.return_value = fetchall_return
    mysql_storage = MySQLDBStorage(db_connect=mocked_db_connect)
    mocker.patch.object(
        MySQLDBStorage, "gen_entity_specific_mysql_fields", return_value=""
    )

    mysql_storage.create_table_if_not_exist(test_x4_entity)  # act
    print(mocked_db_cursor.execute.calls())

    mocked_db_cursor.fetchall.assert_called_once()
    mocked_db_cursor.execute.assert_has_calls(
        [mocker.call("SHOW TABLES"), mocker.call(TEST_CREATE_TABLE_SQL_COMMAND)]
    )
