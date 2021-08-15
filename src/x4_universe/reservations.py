from dataclasses import dataclass
from typing import List, Optional

from x4_universe.entity import X4Entity


@dataclass
class X4EntityReservationRow:
    """Конкретная запись в торговом контракте вселенной X4."""

    ware: Optional[str]
    price: Optional[str]
    amount: Optional[str]
    desired: Optional[str]


@dataclass
class X4EntityReservations(X4Entity):
    """Торговый контракт вселенной X4."""

    rows: List[X4EntityReservationRow]

    def __repr__(self) -> str:
        """Вывод сущности в виде строки."""
        lines = ''.join(
            [
                (
                    f"    {row.ware} price( {row.price} )"
                    f" amount( {row.amount} ) desired( {row.desired} )\n"
                )
                for row in self.rows
            ]
        )

        return f"{self.entity_type} {self.entity_code}:\n" + lines
