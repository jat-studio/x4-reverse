from abc import ABC

from x4_universe.entity import X4Entity


class AbstractStorage(ABC):
    """Абстрактное хранилище для сохранения результатов парсинга."""

    def save(self, entity: X4Entity) -> None:
        """Сохранение полученных данных в хранилище.
        
        Args:
            entity: Объект вселенной X4.
        """
