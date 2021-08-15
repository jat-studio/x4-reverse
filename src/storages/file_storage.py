from config import (
    out_components_file_name,
    out_stations_construction_file_name,
    out_ship_trade_orders_file_name,
    out_trade_offers_file_name,
    out_trade_reservations_file_name,
)
from storages.abstract import AbstractStorage
from x4_universe.entity import X4Entity


class FileStorage(AbstractStorage):
    """Абстрактное хранилище для сохранения результатов парсинга."""

    def save(self, entity: X4Entity) -> None:
        """Сохранение полученных данных в файл.

        Args:
            entity: Объект вселенной X4.
        """
        filepath = out_components_file_name

        if entity.__class__.__name__ == "X4EntityTrade":
            filepath = out_trade_offers_file_name

        if entity.__class__.__name__ == "X4EntityReservations":
            filepath = out_trade_reservations_file_name

        if entity.__class__.__name__ == "X4EntityStation":
            filepath = out_stations_construction_file_name

        if entity.__class__.__name__ in ["X4EntityOrders", "X4EntityEvents"]:
            filepath = out_ship_trade_orders_file_name

        with open(filepath, "a") as save_file:
            save_file.write(str(entity))
