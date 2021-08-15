from typing import Optional

import xml.etree.ElementTree as ET

from x4_save_processor.config import (
    out_trade_offers_file_name,
    out_trade_reservations_file_name,
)


class ETTrade():
    """Парсер тэга trade в ElementTree."""

    def __init__(self, component_type: str, code: str, data: ET) -> None:
        self.component_type = component_type
        self.code = code

        try:
            self.data = data.find("trade")
        except AttributeError:
            self.data = None

    @staticmethod
    def _get_offer_type(trade: ET) -> str:
        """Получение типа предложения: покупка или продажа."""
        offer_type = ""

        if trade.attrib.get("buyer"):
            offer_type = "buyer"

        if trade.attrib.get("seller"):
            offer_type = "seller"

        return offer_type

    def _parse_offers(self) -> None:
        """Парсинг тэга offers внутри trade."""
        try:
            trades = self.data.find("offers").find("production")
        except AttributeError:
            trades = []

        if trades:
            with open(out_trade_offers_file_name, "a") as offers_file:
                offers_file.write(f"{self.component_type} {self.code}:\n")
                [
                    offers_file.write(
                        f"    {self._get_offer_type(trade)}"
                        f" {trade.attrib.get('ware')}"
                        f" price( {trade.attrib.get('price')} )"
                        f" amount( {trade.attrib.get('amount')} )"
                        f" desired( {trade.attrib.get('desired')} )\n"
                    )
                    for trade in trades
                ]

    def _parse_prices(self) -> None:
        """Парсинг тэга prices внутри trade."""
        pass

    def _parse_reservations(self) -> None:
        """Парсинг тэга reservations внутри trade."""
        try:
            reservations = self.data.find("reservations")
        except AttributeError:
            reservations = []

        if reservations:
            with open(out_trade_reservations_file_name, "a") as res_file:
                res_file.write(f"{self.component_type} {self.code}:\n")
                [
                    res_file.write(
                        f"    {reservation.attrib.get('ware')}"
                        f" price( {reservation.attrib.get('price')} )"
                        f" amount( {reservation.attrib.get('amount')} )"
                        f" desired( {reservation.attrib.get('desired')} )\n"
                    )
                    for reservation in reservations
                ]

    def parse(self) -> None:
        """Парсинг тэга trade в ElementTree."""
        self._parse_offers()
        self._parse_prices()
        self._parse_reservations()
