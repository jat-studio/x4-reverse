import pytest
from typing import Callable, Tuple

from src.storages.db_storage import MySQLDBStorage
from src.x4_universe.entity import X4Entity


@pytest.fixture(scope="function")
def mocked_db(mocker) -> Tuple[Callable, Callable]:
    """Мокирование запросов в БД, возвращает мокированный коннект и курсор."""
    mocked_db_connect = mocker.Mock()
    mocked_db_cursor = mocker.Mock()
    mocked_db_connect.cursor.return_value = mocked_db_cursor
    mocker.patch.object(MySQLDBStorage, "get_tables_list_from_db", return_value=[])

    return mocked_db_connect, mocked_db_cursor


@pytest.fixture(scope="function")
def test_mysql_storage(mocker) -> MySQLDBStorage:
    """Тестовый mysql_storage с мокированными запросами к БД."""
    mocker.patch.object(MySQLDBStorage, "get_tables_list_from_db", return_value=[])

    return MySQLDBStorage(db_connect=mocker.Mock())


@pytest.fixture(scope="function")
def test_x4_entity() -> X4Entity:
    """Тестовая сущность вселенной X4."""
    return X4Entity(entity_type="test_type", entity_code="AVS-122")
