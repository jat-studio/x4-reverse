from storages.abstract import AbstractStorage
from x4_save_processor.component.main import ETComponent
from x4_universe.entity import X4Entity
from x4_universe.orders import X4EntityOrderRow, X4EntityOrders


class ETComponentShip(ETComponent):
    """Парсер тэга component типа ship_* в ElementTree."""

    def get_optional_trade_entity(self) -> X4Entity:
        """Получение дополнительных торговых данных в компоненте."""
        orders = X4EntityOrders(
            entity_code=self.code, entity_type=self.component_type, rows=[]
        )

        for order in self.data.find("orders") or []:
            order_trade = order.find("trade")

            if order_trade:
                orders.rows.append(
                    X4EntityOrderRow(
                        order=order.attrib['order'],
                        ware=order_trade.attrib['ware'],
                        price=order_trade.attrib['price'],
                        amount=order_trade.attrib['amount'],
                        desired=order_trade.attrib['desired'],
                    )
                )

        return orders

    def parse(self, storage: AbstractStorage) -> None:
        """Парсинг корабля."""
        self.parse_optional_trade_data(storage)
        self.parse_trade(storage)
