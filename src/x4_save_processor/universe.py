import xml.etree.ElementTree as ET

from storages.abstract import AbstractStorage
from x4_save_processor.component.factory import create_component
from x4_universe.component import X4EntityComponent


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
        self, component_data: ET, depth_counter: int, storage: AbstractStorage
    ) -> None:
        """Рекурсивный парсинг тэгов component."""
        component = component_data.find("component")

        if component:
            et_component = create_component(component)
            et_component.parse(storage)

            storage.save(
                X4EntityComponent(
                    entity_type=et_component.component_type,
                    entity_code=et_component.code,
                    depth_counter=depth_counter,
                    connection=component.attrib.get('connection'),
                )
            )

            component_connections = component.find("connections")
            if component_connections:
                depth_counter += 4
                [
                    self._parse_component_recurse(
                        component_data=connection,
                        depth_counter=depth_counter,
                        storage=storage,
                    )
                    for connection in component_connections
                ]

    def _parse_physics(self) -> None:
        """Парсинг тэга physics."""
        pass

    def process(self, storage: AbstractStorage) -> None:
        """Обработка тэга, запись результатов."""
        self._parse_factions()
        self._parse_jobs()

        self._parse_component_recurse(
            component_data=self.data, depth_counter=0, storage=storage
        )

        self._parse_physics()
