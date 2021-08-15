import xml.etree.ElementTree as ET

from storages.abstract import AbstractStorage
from x4_universe.reservations import (
    X4EntityReservationRow,
    X4EntityReservations,
)
from x4_universe.trade import X4EntityTrade, X4EntityTradeRow


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

    def _parse_offers(self, storage: AbstractStorage) -> None:
        """Парсинг тэга offers внутри trade."""
        try:
            trades = self.data.find("offers").find("production")
        except AttributeError:
            trades = []

        if trades:
            storage.save(
                X4EntityTrade(
                    entity_code=self.code,
                    entity_type=self.component_type,
                    rows=[
                        X4EntityTradeRow(
                            offer_type=self._get_offer_type(trade),
                            ware=trade.attrib.get('ware'),
                            price=trade.attrib.get('price'),
                            amount=trade.attrib.get('amount'),
                            desired=trade.attrib.get('desired'),
                        )
                        for trade in trades
                    ],
                )
            )

    def _parse_prices(self) -> None:
        """Парсинг тэга prices внутри trade."""
        pass

    def _parse_reservations(self, storage: AbstractStorage) -> None:
        """Парсинг тэга reservations внутри trade."""
        try:
            reservations = self.data.find("reservations")
        except AttributeError:
            reservations = []

        if reservations:
            storage.save(
                X4EntityReservations(
                    entity_type=self.component_type,
                    entity_code=self.code,
                    rows=[
                        X4EntityReservationRow(
                            ware=reservation.attrib.get('ware'),
                            price=reservation.attrib.get('price'),
                            amount=reservation.attrib.get('amount'),
                            desired=reservation.attrib.get('desired'),
                        )
                        for reservation in reservations
                    ],
                )
            )

    def parse(self, storage: AbstractStorage) -> None:
        """Парсинг тэга trade в ElementTree."""
        self._parse_offers(storage)
        self._parse_prices()
        self._parse_reservations(storage)
