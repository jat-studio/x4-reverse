from typing import List

import xml.etree.ElementTree as ET

from x4_save_processor.component.trade import ETTrade


class ETComponent():
    """Парсер тэга component в ElementTree."""

    def __init__(self, data: ET) -> None:
        self.data = data
        self.component_type = self.data.attrib["class"]
        self.code = self.data.attrib.get("code")

    def get_optional_trade_data(self) -> List[str]:
        """Получение списка дополнительных торговых данных в компоненте."""
        return []

    def parse_optional_trade_data(self, out_file_name: str) -> None:
        """Парсинг дополнительных торговых данных в компоненте."""
        trade_data = self.get_optional_trade_data()
        if trade_data:
            with open(out_file_name, "a") as out_file:
                out_file.writelines(
                    [f"{self.component_type} {self.code}:\n", *trade_data]
                )

    def parse_trade(self) -> None:
        """Парсинг тэга trade в компоненте."""
        ETTrade(self.component_type, self.code, self.data).parse()

    def parse(self) -> None:
        """Парсинг компонента по-умолчанию."""
        self.parse_trade()
