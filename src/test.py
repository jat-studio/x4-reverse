import xml.etree.ElementTree as ET
from storages.file_storage import FileStorage

from x4_save_processor.component.trade import ETTrade


test_xml = (
    '<component class="station" macro="station_gen_factory_base_01_macro" connection="space" code="AWC-317" owner="freesplit" knownto="player" level="0.2" transportdronemode="trade" pendingtransportdronemode="trade" usertransportdronemode="trade" spawntime="0" nameindex="1" id="[0x50f0]">'
    '<trade>'
    '<reservations>'
    '<reservation reserver="[0x529d]" id="[0x407472]" buyer="[0x50f0]" partner="[0x529d]" ware="energycells" price="1588" amount="1700" desired="1700" flags="sellermoneyvirtual|buyermoneyvirtual|invertfactionrestriction">'
    '<source class="production"/>'
    '</reservation>'
    '<reservation reserver="[0x311d4]" id="[0x987673]" buyer="[0x50f0]" partner="[0x311d4]" ware="siliconwafers" price="41900" amount="416" desired="416" flags="sellermoneyvirtual|buyermoneyvirtual|invertfactionrestriction">'
    '<source class="production"/>'
    '</reservation>'
    '<reservation reserver="[0x3dbb2]" id="[0x70679b]" buyer="[0x50f0]" partner="[0x3dbb2]" ware="siliconwafers" price="41900" amount="416" desired="416" flags="sellermoneyvirtual|buyermoneyvirtual|invertfactionrestriction">'
    '<source class="production"/>'
    '</reservation>'
    '</reservations>'
    '<offers>'
    '<production>'
    '<trade id="[0x2d6f]" buyer="[0x50f0]" ware="energycells" price="1138" amount="500" desired="500" flags="invertfactionrestriction">'
    '<source class="production"/>'
    '</trade>'
    '<trade id="[0x841019]" buyer="[0x50f0]" ware="medicalsupplies" price="6873" amount="1575" desired="1575" flags="invertfactionrestriction">'
    '<source class="production"/>'
    '</trade>'
    '<trade id="[0x2d70]" seller="[0x50f0]" ware="microchips" price="107332" amount="689" flags="invertfactionrestriction">'
    '<source class="production"/>'
    '</trade>'
    '<trade id="[0x2d71]" buyer="[0x50f0]" ware="siliconwafers" price="41900" amount="15300" desired="15300" flags="invertfactionrestriction">'
    '<source class="production"/>'
    '</trade>'
    '</production>'
    '</offers>'
    '<prices>'
    '<reference>'
    '<ware ware="medicalsupplies" buy="66" sell="0"/>'
    '<ware ware="siliconwafers" buy="418" sell="0"/>'
    '<ware ware="energycells" buy="16" sell="0"/>'
    '<ware ware="cheltmeat" buy="49" sell="0"/>'
    '<ware ware="scruffinfruits" buy="26" sell="0"/>'
    '</reference>'
    '</prices>'
    '</trade>'
    '</component>'
)

ETTrade("station", "AWC-317", ET.fromstring(test_xml)).parse()
