from typing import Optional

from src.storages.db_storage import MySQLDBStorage
from src.x4_universe.entity import X4Entity


class FakeX4EntityWithAdditionalFieldStr(X4Entity):
    """Фейковый класс основанный на X4Entity.

    Но с дополнительными полями типа str и Optional[str]
    """

    str_field: str
    optional_str_field: Optional[str]


class FakeX4EntityWithAdditionalFieldInt(X4Entity):
    """Фейковый класс основанный на X4Entity.

    Но с дополнительными полями типа int и Optional[int]
    """

    int_field: int
    optional_int_field: Optional[int]


def test_success_for_base_entity(mocker, test_x4_entity) -> None:
    """Генерация дополнительных полей таблицы для базовой сущности."""
    mysql_storage = MySQLDBStorage(db_connect=mocker.Mock())

    result = mysql_storage.gen_entity_specific_mysql_fields(test_x4_entity)

    assert result == ""


def test_success_for_entity_w_str_fields(mocker) -> None:
    """Генерация дополнительных полей таблицы.

    Для сущности с дополнительным полем типа str/Optional[str].
    """
    mysql_storage = MySQLDBStorage(db_connect=mocker.Mock())
    fake_entity = FakeX4EntityWithAdditionalFieldStr(
        entity_type="test_type",
        entity_code="AVS-122",
        str_field="str_field",
        optional_str_field=None,
    )

    result = mysql_storage.gen_entity_specific_mysql_fields(fake_entity)

    assert result == (
        "`optional_str_field` varchar(60) NULL, `str_field` varchar(60) NULL, "
    )


def test_success_for_entity_w_int_fields(mocker) -> None:
    """Генерация дополнительных полей таблицы.

    Для сущности с дополнительным полем типа int/Optional[int].
    """
    mysql_storage = MySQLDBStorage(db_connect=mocker.Mock())
    fake_entity = FakeX4EntityWithAdditionalFieldInt(
        entity_type="test_type",
        entity_code="AVS-122",
        int_field=42,
        optional_int_field=None,
    )

    result = mysql_storage.gen_entity_specific_mysql_fields(fake_entity)

    assert result == "`optional_int_field` int NULL, `int_field` int NULL, "
