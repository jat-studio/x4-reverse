from dataclasses import dataclass
from typing import Optional

from src.x4_universe.entity import X4Entity


@dataclass
class X4EntityComponent(X4Entity):
    """Сущность типа "компонент" вселенной X4."""

    depth_counter: Optional[int]
    connection: Optional[str]

    def __repr__(self) -> str:
        """Вывод сущности в виде строки."""
        return (
            f"{self.depth_counter * ' '}{self.entity_type}:{self.connection}"
            f" {self.entity_code}\n"
        )
