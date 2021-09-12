import pytest
from dataclasses import dataclass
from typing import Optional

from src.storages.db_storage import MySQLDBStorage
from src.x4_universe.entity import X4Entity


@dataclass
class FakeX4EntityWithAdditionalUnknownField(X4Entity):
    """Фейковый класс основанный на X4Entity.

    Но с дополнительным полем неизвестного ранее типа.
    """

    unknown_field: float


@dataclass
class FakeX4EntityWithAdditionalFieldStr(X4Entity):
    """Фейковый класс основанный на X4Entity.

    Но с дополнительными полями типа str и Optional[str]
    """

    str_field: str
    optional_str_field: Optional[str]


@dataclass
class FakeX4EntityWithAdditionalFieldInt(X4Entity):
    """Фейковый класс основанный на X4Entity.

    Но с дополнительными полями типа int и Optional[int]
    """

    int_field: int
    optional_int_field: Optional[int]


def test_fail_for_entity_w_unknown_field_type(mocker, test_mysql_storage) -> None:
    """Генерация дополнительных полей таблицы для базовой сущности."""
    test_entity = FakeX4EntityWithAdditionalUnknownField(
        entity_type="test_type", entity_code="AVS-122", unknown_field=2.2
    )

    with pytest.raises(ValueError):  # act
        test_mysql_storage.gen_entity_specific_mysql_fields(test_entity)


def test_success_for_base_entity(mocker, test_x4_entity, test_mysql_storage) -> None:
    """Генерация дополнительных полей таблицы для базовой сущности."""
    result = test_mysql_storage.gen_entity_specific_mysql_fields(test_x4_entity)

    assert result == ""


def test_success_for_entity_w_str_fields(mocker, test_mysql_storage) -> None:
    """Генерация дополнительных полей таблицы.

    Для сущности с дополнительным полем типа str/Optional[str].
    """
    fake_entity = FakeX4EntityWithAdditionalFieldStr(
        entity_type="test_type",
        entity_code="AVS-122",
        str_field="str_field",
        optional_str_field=None,
    )

    result = test_mysql_storage.gen_entity_specific_mysql_fields(fake_entity)

    assert result == (
        "`optional_str_field` varchar(60) NULL, `str_field` varchar(60) NULL, "
    )


def test_success_for_entity_w_int_fields(mocker, test_mysql_storage) -> None:
    """Генерация дополнительных полей таблицы.

    Для сущности с дополнительным полем типа int/Optional[int].
    """
    fake_entity = FakeX4EntityWithAdditionalFieldInt(
        entity_type="test_type",
        entity_code="AVS-122",
        int_field=42,
        optional_int_field=None,
    )

    result = test_mysql_storage.gen_entity_specific_mysql_fields(fake_entity)

    assert result == "`int_field` int NULL, `optional_int_field` varchar(60) NULL, "
