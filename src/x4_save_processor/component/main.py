from typing import List

import xml.etree.ElementTree as ET

from src.storages.abstract import AbstractStorage
from src.x4_save_processor.component.trade import ETTrade
from src.x4_universe.entity import X4Entity


class ETComponent():
    """Парсер тэга component в ElementTree."""

    def __init__(self, data: ET) -> None:
        self.data = data
        self.component_type = self.data.attrib["class"]
        self.code = self.data.attrib.get("code")

    def get_optional_trade_entity(self) -> X4Entity:
        """Получение дополнительных торговых данных в компоненте."""
        return None

    def parse_optional_trade_data(self, storage: AbstractStorage) -> None:
        """Парсинг дополнительных торговых данных в компоненте."""
        trade_data = self.get_optional_trade_entity()
        if trade_data:
            storage.save(trade_data)

    def parse_trade(self, storage: AbstractStorage) -> None:
        """Парсинг тэга trade в компоненте."""
        ETTrade(self.component_type, self.code, self.data).parse(storage)

    def parse(self, storage: AbstractStorage) -> None:
        """Парсинг компонента по-умолчанию."""
        self.parse_trade(storage)
