import xml.etree.ElementTree as ET

from src.x4_save_processor.component.main import ETComponent
from src.x4_save_processor.component.ship import ETComponentShip
from src.x4_save_processor.component.station import ETComponentStation


COMPONENTS_PARSE_MAP = {
    "ship_l": ETComponentShip,
    "ship_m": ETComponentShip,
    "ship_s": ETComponentShip,
    "ship_xl": ETComponentShip,
    "ship_xs": ETComponentShip,
    "station": ETComponentStation,
}


def create_component(component: ET) -> "ETComponent":
    """Создание экземпляра ETComponent из xml Etree."""
    try:
        return COMPONENTS_PARSE_MAP[component.attrib['class']](component)
    except KeyError:
        return ETComponent(component)
