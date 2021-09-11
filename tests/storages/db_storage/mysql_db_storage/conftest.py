from typing import Any, Tuple
import pytest

from src.x4_universe.entity import X4Entity


@pytest.fixture(scope="function")
def mocked_db(mocker) -> Tuple[Any, Any]:
    """Мокирование запросов в БД, возвращает мокированный коннект и курсор."""
    mocked_db_connect = mocker.Mock()
    mocked_db_cursor = mocker.Mock()
    mocked_db_connect.cursor.return_value = mocked_db_cursor

    return mocked_db_connect, mocked_db_cursor


@pytest.fixture(scope="function")
def test_x4_entity() -> X4Entity:
    """Тестовая сущность вселенной X4."""
    return X4Entity(entity_type="test_type", entity_code="AVS-122")
