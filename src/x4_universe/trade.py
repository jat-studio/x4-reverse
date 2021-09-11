from dataclasses import dataclass
from typing import List, Optional

from src.x4_universe.entity import X4Entity


@dataclass
class X4EntityTradeRow:
    """Конкретная запись в торговом предложении вселенной X4."""

    offer_type: str
    ware: Optional[str]
    price: Optional[str]
    amount: Optional[str]
    desired: Optional[str]


@dataclass
class X4EntityTrade(X4Entity):
    """Торговое предложение вселенной X4."""

    rows: List[X4EntityTradeRow]

    def __repr__(self) -> str:
        """Вывод торгового предложения в виде строки."""
        lines = ''.join(
            [
                (
                    f"    {row.offer_type} {row.ware} price( {row.price} )"
                    f" amount( {row.amount} ) desired( {row.desired} )\n"
                )
                for row in self.rows
            ]
        )

        return f"{self.entity_type} {self.entity_code}:\n" + lines
