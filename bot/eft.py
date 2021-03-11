from __future__ import annotations  # type: ignore
import requests
import requests.utils
from requests.utils import quote  # type: ignore
from typing import Optional, Any, Tuple
from bot.config import settings, localized_string
from bot.models import TarkovMarketModel, AmmoModel, safe_int
from dataclasses import dataclass
import datetime
import maya
import json
import math


class InvalidLocaleError(Exception):
    def __init__(self, locale):
        super().__init__(f"Unknown locale {locale}")
        self.locale = locale


# utility class for interfacing with EFT's data.
class EFT:
    @staticmethod
    def check_armor(lang: str, query: str) -> str:
        armor_link = (
            settings["armor_link"][lang] if lang in settings["armor_link"] else None
        )
        if not armor_link:
            raise InvalidLocaleError(lang)
        crafted_url = armor_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_armorstats(lang: str, query: str) -> str:
        armorstats_link = (
            settings["armorstats_link"][lang]
            if lang in settings["armorstats_link"]
            else None
        )
        if not armorstats_link:
            raise InvalidLocaleError(lang)
        crafted_url = armorstats_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_astat(lang: str, query: str) -> AmmoModel:
        astat_link = (
            settings["astat_link"][lang] if lang in settings["astat_link"] else None
        )
        if not astat_link:
            raise InvalidLocaleError(lang)
        crafted_url = astat_link.format(quote(query), quote(lang))
        response = requests.get(crafted_url).json()
        return AmmoModel.fromJSONObj(response)

    @staticmethod
    def check_avg7d(lang: str, query: str) -> str:
        avg7d_link = (
            settings["avg7d_link"][lang] if lang in settings["avg7d_link"] else None
        )
        if not avg7d_link:
            raise InvalidLocaleError(lang)
        crafted_url = avg7d_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_avg24h(lang: str, query: str) -> str:
        avg24h_link = (
            settings["avg24h_link"][lang] if lang in settings["avg24h_link"] else None
        )
        if not avg24h_link:
            raise InvalidLocaleError(lang)
        crafted_url = avg24h_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_helmets(lang: str, query: str) -> str:
        helmet_link = (
            settings["helmet_link"][lang] if lang in settings["helmet_link"] else None
        )
        if not helmet_link:
            raise InvalidLocaleError(lang)
        crafted_url = helmet_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_helmetstats(lang: str, query: str) -> str:
        helmetstats_link = (
            settings["helmetstats_link"][lang]
            if lang in settings["helmetstats_link"]
            else None
        )
        if not helmetstats_link:
            raise InvalidLocaleError(lang)
        crafted_url = helmetstats_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_kappaquest(lang: str, query: str) -> str:
        kappaquest_link = (
            settings["kappaquest_link"][lang]
            if lang in settings["kappaquest_link"]
            else None
        )
        if not kappaquest_link:
            raise InvalidLocaleError(lang)
        crafted_url = kappaquest_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_kappaitem(lang: str, query: str) -> str:
        kappaitem_link = (
            settings["kappaitem_link"][lang]
            if lang in settings["kappaitem_link"]
            else None
        )
        if not kappaitem_link:
            raise InvalidLocaleError(lang)
        crafted_url = kappaitem_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_medical(lang: str, query: str) -> str:
        medical_link = (
            settings["medical_link"][lang] if lang in settings["medical_link"] else None
        )
        if not medical_link:
            raise InvalidLocaleError(lang)
        crafted_url = medical_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_profit(lang: str, query: str) -> str:
        profit_link = (
            settings["profit_link"][lang] if lang in settings["profit_link"] else None
        )
        if not profit_link:
            raise InvalidLocaleError(lang)
        crafted_url = profit_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_price(lang: str, query: str) -> TarkovMarketModel:
        price_link = (
            settings["price_link"][lang] if lang in settings["price_link"] else None
        )
        if not price_link:
            raise InvalidLocaleError(lang)
        crafted_url = price_link.format(quote(query), quote(lang))
        response = requests.get(crafted_url).json()
        return TarkovMarketModel.fromJSONObj(response)

    @staticmethod
    def check_slot(lang: str, query: str) -> str:
        slot_link = (
            settings["slot_link"][lang] if lang in settings["slot_link"] else None
        )
        if not slot_link:
            raise InvalidLocaleError(lang)
        crafted_url = slot_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_trader(lang: str, query: str) -> str:
        trader_link = (
            settings["trader_link"][lang] if lang in settings["trader_link"] else None
        )
        if not trader_link:
            raise InvalidLocaleError(lang)
        crafted_url = trader_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_wiki(lang: str, query: str) -> str:
        wiki_link = (
            settings["wiki_link"][lang] if lang in settings["wiki_link"] else None
        )
        if not wiki_link:
            raise InvalidLocaleError(lang)
        crafted_url = wiki_link.format(quote(query))
        response = requests.get(crafted_url).text
        return response.strip()

    @staticmethod
    def check_tax(
        lang: str, requestValue: int, query: str
    ) -> Optional[Tuple[int, TarkovMarketModel]]:
        """
        Returns the computed tax, or None if there was an error.
        """
        price = EFT.check_price(lang, query)
        if not price:
            return None
        offerModifier = math.log10(float(price.basePrice) / requestValue)
        requestModifier = math.log10(requestValue / float(price.basePrice))
        if requestValue >= price.basePrice:
            requestModifier = pow(requestModifier, 1.08)
        else:
            offerModifier = pow(offerModifier, 1.08)
        tax = price.basePrice * 0.05 * pow(
            4, offerModifier
        ) + requestValue * 0.05 * pow(4, requestModifier)
        return (math.floor(tax), price)
