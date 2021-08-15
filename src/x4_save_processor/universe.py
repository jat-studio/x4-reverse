from typing import IO

import xml.etree.ElementTree as ET

from x4_save_processor.config import out_components_file_name
from x4_save_processor.component.factory import create_component


class ETUniverse():
    """Парсер тэга universe в ElementTree."""

    def __init__(self, save_file_name: str) -> None:
        self.data = ET.parse(save_file_name).getroot().find("universe")

    def _parse_factions(self) -> None:
        """Парсинг тэга factions."""
        pass

    def _parse_jobs(self) -> None:
        """Парсинг тэга jobs."""
        pass

    def _parse_component_recurse(
        self, component_data: ET, depth_counter: int, components_file: IO
    ) -> None:
        """Рекурсивный парсинг тэгов component."""
        component = component_data.find("component")

        if component:
            et_component = create_component(component)
            et_component.parse()

            components_file.write(
                f"{depth_counter * ' '}"
                f"{et_component.component_type}:"
                f"{component.attrib.get('connection')}"
                f" {et_component.code}\n"
            )

            component_connections = component.find("connections")
            if component_connections:
                depth_counter += 4
                [
                    self._parse_component_recurse(
                        connection, depth_counter, components_file
                    )
                    for connection in component_connections
                ]

    def _parse_physics(self) -> None:
        """Парсинг тэга physics."""
        pass

    def process(self) -> None:
        """Обработка тэга, запись результатов."""
        self._parse_factions()
        self._parse_jobs()

        with open(out_components_file_name, "w") as components_file:
            self._parse_component_recurse(self.data, 0, components_file)

        self._parse_physics()
