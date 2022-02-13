from __future__ import annotations  # type: ignore
from typing import Any
from bot.config import settings
from dataclasses import dataclass
import datetime
import maya


def safe_int(value: Any, fallback: int) -> int:
    try:
        return int(value)
    except:
        return fallback


@dataclass
class KappaItemsModel:
    name: str
    quantity: int

    @classmethod
    def fromJSONObj(cls, object: Any) -> KappaItemsModel:
        return KappaItemsModel(
            name=object.get("name"),
            quantity=object.get("itemQTY"),
        )


@dataclass
class KappaQuestsModel:
    name: str
    isReq: int

    @classmethod
    def fromJSONObj(cls, object: Any) -> KappaQuestsModel:
        return KappaQuestsModel(
            name=object.get("name"),
            isReq=object.get("kappaReq"),
        )

############

@dataclass
class tcArmorModel:
    name: str
    bsgID: str
    armorClass: str
    armorMats: str
    armorZones: str
    maxDurability: str
    effectiveDurability: str
    moveSpeedPen: str
    turnSpeedPen: str
    ergoPen: str
    tcLink: str


    @classmethod
    def fromJSONObj(cls, object: Any) -> tcArmorModel:
        return tcArmorModel(
            name=object.get("Name"),
            bsgID=object.get("Item ID"),
            armorClass=object.get("Armor Class"),
            armorMats=object.get("Armor Material"),
            armorZones=object.get("Protection Zones"),
            maxDurability=object.get("Max Durability"),
            effectiveDurability=object.get("Effective Durability"),
            moveSpeedPen=object.get("Movement Speed Penalty"),
            turnSpeedPen=object.get("Turn Speed Penalty"),
            ergoPen=object.get("Ergonomics Penalty"),
            tcLink=object.get("URL"),
        )

@dataclass
class tcHelmetModel:
    name: str
    bsgID: str
    armorClass: str
    armorMats: str
    blindProtect: str
    blocksEar: str
    blocksEye: str
    blocksFace: str
    blocksHead: str
    bluntThroughput: str
    armorDurability: str
    armorRepair: str
    armorZones: str
    armorSegments: str
    armorMoveSpeed: str
    armorTurnSpeed: str
    armorErgo: str
    cellHeight: str
    cellWidth: str
    itemWeight: str
    maxStackSize: str


    @classmethod
    def fromJSONObj(cls, object: Any) -> tcHelmetModel:
        return tcHelmetModel(
            name=object.get("Name"),
            bsgID=object.get("Item ID"),
            armorClass=object.get("Armor Class"),
            armorMats=object.get("Materials"),
            blindProtect=object.get("Blindness Protection"),
            blocksEar=object.get("Blocks Earpiece"),
            blocksEye=object.get("Blocks Eyewear"),
            blocksFace=object.get("Blocks FaceCover"),
            blocksHead=object.get("Blocks Head"),
            bluntThroughput=object.get("Blunt Throughput"),
            armorDurability=object.get("Max Durability"),
            armorRepair=object.get("Repair Cost"),
            armorZones=object.get("Protection Zones"),
            armorSegments=object.get("Armor Segments"),
            armorMoveSpeed=object.get("Movement Speed Penalty"),
            armorTurnSpeed=object.get("Turn Speed Penalty"),
            armorErgo=object.get("Ergonomics Penalty"),
            cellHeight=object.get("Cell Height"),
            cellWidth=object.get("Cell Width"),
            itemWeight=object.get("Item Weight"),
            maxStackSize=object.get("Max Stack Size"),
            
        )

@dataclass
class tcAmmoModel:
    name: str
    bsgID: str
    caliber: str
    fleshDmg: str
    penPower: str
    armorDmg: str
    ammoAcc: str
    ammoRec: str
    ammoFrag: str
    bulletVelocity: str
    misfire: str
    penChance: str
    heavyBleed: str
    lightBleed: str
    ballisticCoeff: str
    cellHeight: str
    cellWidth: str
    itemWeight: str
    maxStackSize: str

    @classmethod
    def fromJSONObj(cls, object: Any) -> tcHelmetModel:
        return tcAmmoModel(
            name=object.get("Name"),
            bsgID=object.get("Item ID"),
            caliber=object.get("Caliber"),
            fleshDmg=object.get("Flesh Damage"),
            penPower=object.get("Penetration Power"),
            armorDmg=object.get("Armor Damage"),
            ammoAcc=object.get("Accuracy"),
            ammoRec=object.get("Recoil"),
            ammoFrag=object.get("Frag Chance"),
            bulletVelocity=object.get("Projectile Speed"),
            misfire=object.get("Misfire Chance"),
            penChance=object.get("Penetration Chance"),
            heavyBleed=object.get("Heavy Bleeding Delta"),
            lightBleed=object.get("Light Bleeeding Delta"),
            ballisticCoeff=object.get("Ballistic Coefficient"),
            cellHeight=object.get("Cell Height"),
            cellWidth=object.get("Cell Width"),
            itemWeight=object.get("Item Weight"),
            maxStackSize=object.get("Max Stack Size"),
        )

"""
Need to do following models:
Maps, Medical Items
"""

@dataclass
class TarkovMarketModel:
    name: str
    shortName: str
    price: int
    basePrice: int
    avg24hPrice: int
    avg7daysPrice: int
    traderName: str
    traderPrice: int
    updated: datetime.datetime
    slots: int
    img: str
    wikiLink: str

    @classmethod
    def fromJSONObj(cls, object: Any) -> TarkovMarketModel:
        return TarkovMarketModel(
            name=object.get("name"),
            shortName=object.get("shortName"),
            price=object.get("price"),
            basePrice=object.get("basePrice"),
            avg24hPrice=object.get("avg24hPrice"),
            avg7daysPrice=object.get("avg7daysPrice"),
            traderName=object.get("traderName"),
            traderPrice=object.get("traderPrice"),
            updated=maya.parse(object.get("updated")).datetime(),
            slots=object.get("slots"),
            img=object.get("img"),
            wikiLink=object.get("wikiLink"),
        )