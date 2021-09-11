import re
from typing import Dict, List, Union
import MySQLdb
import os
import yaml

from src.storages.abstract import AbstractStorage
from src.x4_universe.entity import X4Entity

DB_ACCESS_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "db_access.yaml"
)


def get_db_access_params(
    config_path: str = DB_ACCESS_FILE_PATH
) -> Dict[str, Union[int, str]]:
    """Получение параметров доступа к БД."""
    with open(config_path, "r") as cp:
        return yaml.safe_load(cp)


class MySQLDBStorage(AbstractStorage):
    """Хранилище для сохранения результатов парсинга в базе данных."""

    db = MySQLdb.connect(**get_db_access_params())

    def _get_tables_list(self) -> List[str]:
        """Получение списка таблиц в БД."""
        cursor = self.db.cursor()

        cursor.execute("SHOW TABLES")
        try:
            return cursor.fetchall()[0]
        except IndexError:
            return []

    def gen_entity_specific_mysql_fields(self, entity: X4Entity) -> str:
        """Генерация полей таблицы для информации по конкретной сущности.

        Args:
            entity: Объект вселенной X4.

        Returns:
            Строка со структурой специфичных для сущности полей в таблице БД.
        """
        return ""

    def create_table_if_not_exist(self, entity: X4Entity) -> None:
        """Динамическое создание таблицы, если таблица ещё не существует.

        Args:
            entity: Объект вселенной X4.
        """
        if entity.entity_type in self._get_tables_list():
            return

        cursor = self.db.cursor()
        cursor.execute(
            f"CREATE TABLE `{entity.entity_type}` ( "
            "`id` int NOT NULL AUTO_INCREMENT, "
            "`code` varchar(8) NOT NULL, "
            f"{self.gen_entity_specific_mysql_fields(entity)}"
            "PRIMARY KEY (`id`), "
            "UNIQUE KEY `code` (`code`) "
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"
        )

    def insert_entity_to_table(self, entity: X4Entity) -> None:
        """Добавление данных о сущности в таблицу БД.

        Args:
            entity: Объект вселенной X4.
        """
        pass

    def save(self, entity: X4Entity) -> None:
        """Сохранение полученных данных в БД.

        Args:
            entity: Объект вселенной X4.
        """
        self.create_table_if_not_exist(entity)
        self.insert_entity_to_table(entity)
