from dataclasses import dataclass
from typing import List

from x4_universe.entity import X4Entity


@dataclass
class X4EntityStationConstruction:
    """Модуль космической станции вселенной X4."""

    index: str
    macro: str


@dataclass
class X4EntityStation(X4Entity):
    """Космическая станция вселенной X4."""

    constructions: List[X4EntityStationConstruction]

    def __repr__(self) -> str:
        """Вывод сущности в виде строки."""
        lines = ''.join(
            [f"    {row.index} - {row.macro}\n" for row in self.constructions]
        )

        return f"{self.entity_type} {self.entity_code}:\n" + lines
