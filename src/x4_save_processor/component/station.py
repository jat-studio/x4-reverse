from storages.abstract import AbstractStorage
from x4_save_processor.component.main import ETComponent
from x4_universe.entity import X4Entity
from x4_universe.events import X4EntityEventRow, X4EntityEvents
from x4_universe.station import X4EntityStation, X4EntityStationConstruction


class ETComponentStation(ETComponent):
    """Парсер тэга component типа station в ElementTree."""

    def get_optional_trade_entity(self) -> X4Entity:
        """Получение дополнительных торговых данных в компоненте."""
        events = X4EntityEvents(
            entity_code=self.code, entity_type=self.component_type, rows=[]
        )

        for event in self.data.find("events") or []:
            trade_event = event.find("trade")

            if trade_event:
                events.rows.append(
                    X4EntityEventRow(
                        event=event.attrib['event'],
                        ware=trade_event.attrib['ware'],
                        price=trade_event.attrib['price'],
                        amount=trade_event.attrib['amount'],
                        desired=trade_event.attrib['desired'],
                        escrow=trade_event.attrib.get('escrow'),
                    )
                )

        return events

    def _parse_constuction(self, storage: AbstractStorage) -> None:
        """Парсинг модулей конструкции станции."""
        raw_sequences = self.data.find("construction").find("sequence") or []
        storage.save(
            X4EntityStation(
                entity_type=self.component_type,
                entity_code=self.code,
                constructions=[
                    X4EntityStationConstruction(
                        index=entry.attrib['index'],
                        macro=entry.attrib['macro'],
                    )
                    for entry in raw_sequences
                ],
            )
        )

    def parse(self, storage: AbstractStorage) -> None:
        """Парсинг станции."""
        self.parse_optional_trade_data(storage)
        self._parse_constuction(storage)
        self.parse_trade(storage)
