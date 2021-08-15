from dataclasses import dataclass
from typing import List, Optional

from x4_universe.entity import X4Entity


@dataclass
class X4EntityEventRow:
    """Конкретная запись в торговых событиях вселенной X4."""

    event: str
    ware: str
    price: str
    amount: str
    desired: str
    escrow: Optional[str]


@dataclass
class X4EntityEvents(X4Entity):
    """Торговые события вселенной X4."""

    rows: List[X4EntityEventRow]

    def __repr__(self) -> str:
        """Вывод сущности в виде строки."""
        lines = ''.join(
            [
                (
                    f"    {row.event} {row.ware} price( {row.price} )"
                    f" escrow( {row.escrow} ) amount( {row.amount} )"
                    f" desired( {row.desired} )\n"
                )
                for row in self.rows
            ]
        )

        return f"{self.entity_type} {self.entity_code}:\n" + lines
