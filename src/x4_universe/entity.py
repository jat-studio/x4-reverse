from dataclasses import dataclass
from typing import Optional


@dataclass
class X4Entity:
    """Базовая сущность объектов вселенной X4."""

    entity_type: str
    entity_code: str

    def __repr__(self) -> str:
        """Вывод базовой сущности в виде строки."""
        raise NotImplementedError
