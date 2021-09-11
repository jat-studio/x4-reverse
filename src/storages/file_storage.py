from src.storages.abstract import AbstractStorage
from src.x4_universe.entity import X4Entity


out_components_file_name = "D:/X4_reverse/components.txt"
out_ship_trade_orders_file_name = "D:/X4_reverse/ship_trade_orders.txt"
out_stations_construction_file_name = "D:/X4_reverse/stations_construction.txt"
out_stations_trade_events_file_name = "D:/X4_reverse/stations_trade_events.txt"
out_trade_offers_file_name = "D:/X4_reverse/trade_offers.txt"
out_trade_reservations_file_name = "D:/X4_reverse/trade_reservations.txt"


class FileStorage(AbstractStorage):
    """Файловое хранилище для сохранения результатов парсинга."""

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
