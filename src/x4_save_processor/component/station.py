from typing import List

from x4_save_processor.config import (
    out_stations_construction_file_name,
    out_stations_trade_events_file_name,
)
from x4_save_processor.component.main import ETComponent


class ETComponentStation(ETComponent):
    """Парсер тэга component типа station в ElementTree."""

    def get_optional_trade_data(self) -> List[str]:
        """Получение списка дополнительных торговых данных в компоненте."""
        trade_events = []

        for event in self.data.find("events") or []:
            trade_event = event.find("trade")

            if trade_event:
                trade_events.append(
                    f"    {event.attrib['event']}"
                    f" {trade_event.attrib['ware']}"
                    f" price( {trade_event.attrib['price']} )"
                    f" escrow( {trade_event.attrib.get('escrow')} )"
                    f" amount( {trade_event.attrib['amount']} )"
                    f" desired( {trade_event.attrib['desired']} )\n"
                )

        return trade_events

    def _parse_constuction(self) -> None:
        """Парсинг модулей конструкции станции."""
        with open(out_stations_construction_file_name, "a") as constr_file:
            constr_file.write(f"{self.component_type} {self.code}:\n")
            for entry in self.data.find("construction").find("sequence") or []:
                constr_file.write(
                    f"    {entry.attrib['index']} - {entry.attrib['macro']}\n"
                )

    def parse(self) -> None:
        """Парсинг станции."""
        self.parse_optional_trade_data(out_stations_trade_events_file_name)
        self._parse_constuction()
        self.parse_trade()
