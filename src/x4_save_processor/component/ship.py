from typing import List

from x4_save_parser.config import out_ship_trade_orders_file_name
from x4_save_parser.component.main import ETComponent


class ETComponentShip(ETComponent):
    """Парсер тэга component типа ship_* в ElementTree."""

    def get_optional_trade_data(self) -> List[str]:
        """Получение списка дополнительных торговых данных в компоненте."""
        trade_orders = []

        for order in self.data.find("orders") or []:
            order_trade = order.find("trade")

            if order_trade:
                trade_orders.append(
                    f"    {order.attrib['order']}"
                    f" {order_trade.attrib['ware']}"
                    f" price( {order_trade.attrib['price']} )"
                    f" amount( {order_trade.attrib['amount']} )"
                    f" desired( {order_trade.attrib['desired']} )\n"
                )

        return trade_orders

    def parse(self) -> None:
        """Парсинг корабля."""
        self.parse_optional_trade_data(out_ship_trade_orders_file_name)
        self.parse_trade()
