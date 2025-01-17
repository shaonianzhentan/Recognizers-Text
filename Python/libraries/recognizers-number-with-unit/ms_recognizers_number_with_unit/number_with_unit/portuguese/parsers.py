#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ms_recognizers_text.culture import Culture
from ms_recognizers_text.extractor import Extractor
from ms_recognizers_text.parser import Parser
from ms_recognizers_number.culture import CultureInfo
from ms_recognizers_number.number.portuguese.extractors import PortugueseNumberExtractor, NumberMode
from ms_recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from ms_recognizers_number.number.portuguese.parsers import PortugueseNumberParserConfiguration
from ms_recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from ms_recognizers_number_with_unit.resources.portuguese_numeric_with_unit import PortugueseNumericWithUnit


class PortugueseNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):
    @property
    def internal_number_parser(self) -> Parser:
        return self._internal_number_parser

    @property
    def internal_number_extractor(self) -> Extractor:
        return self._internal_number_extractor

    @property
    def connector_token(self) -> str:
        return PortugueseNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Portuguese)
        super().__init__(culture_info)
        self._internal_number_extractor = PortugueseNumberExtractor(
            NumberMode.DEFAULT)
        self._internal_number_parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, PortugueseNumberParserConfiguration(culture_info))


class PortugueseAgeParserConfiguration(PortugueseNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.AgeSuffixList)


class PortugueseCurrencyParserConfiguration(PortugueseNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = PortugueseNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = PortugueseNumericWithUnit.FractionalUnitNameToCodeMap


class PortugueseDimensionParserConfiguration(PortugueseNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.InformationSuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.AreaSuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.LengthSuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.SpeedSuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.VolumeSuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.WeightSuffixList)


class PortugueseTemperatureParserConfiguration(PortugueseNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.TemperatureSuffixList)
