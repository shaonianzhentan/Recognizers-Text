#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ms_recognizers_text.culture import Culture
from ms_recognizers_text.extractor import Extractor
from ms_recognizers_text.parser import Parser
from ms_recognizers_number.culture import CultureInfo
from ms_recognizers_number.number.spanish.extractors import SpanishNumberExtractor, NumberMode
from ms_recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from ms_recognizers_number.number.spanish.parsers import SpanishNumberParserConfiguration
from ms_recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from ms_recognizers_number_with_unit.resources.spanish_numeric_with_unit import SpanishNumericWithUnit


class SpanishNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):
    @property
    def internal_number_parser(self) -> Parser:
        return self._internal_number_parser

    @property
    def internal_number_extractor(self) -> Extractor:
        return self._internal_number_extractor

    @property
    def connector_token(self) -> str:
        return SpanishNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Spanish)
        super().__init__(culture_info)
        self._internal_number_extractor = SpanishNumberExtractor(
            NumberMode.DEFAULT)
        self._internal_number_parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, SpanishNumberParserConfiguration(culture_info))


class SpanishAgeParserConfiguration(SpanishNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.AgeSuffixList)


class SpanishCurrencyParserConfiguration(SpanishNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = SpanishNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = SpanishNumericWithUnit.FractionalUnitNameToCodeMap


class SpanishDimensionParserConfiguration(SpanishNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.InformationSuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.AreaSuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.LengthSuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.SpeedSuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.VolumeSuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.WeightSuffixList)


class SpanishTemperatureParserConfiguration(SpanishNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.TemperatureSuffixList)
