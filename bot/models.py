from __future__ import annotations  # type: ignore
import requests
import requests
import requests.utils
import requests.utils
from requests.utils import quote  # type: ignore
from requests.utils import quote  # type: ignore
from typing import Optional
from typing import Optional, Any
from bot.config import settings
from dataclasses import dataclass
import datetime
import maya
import json


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

"""
Need to do following models:
Ammo, Helmet, Maps, Medical Items, 1-2 more(?)
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