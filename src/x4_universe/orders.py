from dataclasses import dataclass
from typing import List

from x4_universe.entity import X4Entity


@dataclass
class X4EntityOrderRow:
    """Конкретная запись в торговых приказах вселенной X4."""

    order: str
    ware: str
    price: str
    amount: str
    desired: str


@dataclass
class X4EntityOrders(X4Entity):
    """Торговый приказ вселенной X4."""

    rows: List[X4EntityOrderRow]

    def __repr__(self) -> str:
        """Вывод сущности в виде строки."""
        lines = ''.join(
            [
                (
                    f"    {row.order} {row.ware} price( {row.price} )"
                    f" amount( {row.amount} ) desired( {row.desired} )\n"
                )
                for row in self.rows
            ]
        )

        return f"{self.entity_type} {self.entity_code}:\n" + lines
