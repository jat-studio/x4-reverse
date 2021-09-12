import pytest

from src.storages.db_storage import MySQLDBStorage


@pytest.mark.parametrize(
    "fetch_tables, expected_result",
    (
        ((), []),
        ((('test_table',),), ("test_table",)),
    ),
    ids=("w_empty_tables_list", "w_one_item_in_tables_list")
)
def test_success(mocker, fetch_tables, expected_result) -> None:
    """Успешное получение списка таблиц в БД."""
    mocked_db_connect = mocker.Mock()
    mocked_db_cursor = mocker.Mock()
    mocked_db_connect.cursor.return_value = mocked_db_cursor
    mocked_db_cursor.fetchall.return_value = fetch_tables
    mysql_storage = MySQLDBStorage(db_connect=mocked_db_connect)

    result = mysql_storage.get_tables_list_from_db()

    assert result == expected_result
