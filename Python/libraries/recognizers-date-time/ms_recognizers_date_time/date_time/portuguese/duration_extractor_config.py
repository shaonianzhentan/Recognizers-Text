#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern

from ms_recognizers_text.utilities import RegExpUtility
from ms_recognizers_number.number.extractors import BaseNumberExtractor
from ms_recognizers_number.number.portuguese.extractors import PortugueseCardinalExtractor
from ...resources.portuguese_date_time import PortugueseDateTime
from ..base_duration import DurationExtractorConfiguration


class PortugueseDurationExtractorConfiguration(DurationExtractorConfiguration):

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def special_number_unit_regex(self):
        return self._special_number_unit_regex

    @property
    def check_both_before_after(self):
        return self._check_both_before_after

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def all_regex(self) -> Pattern:
        return self._all_regex

    @property
    def half_regex(self) -> Pattern:
        return self._half_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def an_unit_regex(self) -> Pattern:
        return self._an_unit_regex

    @property
    def inexact_number_unit_regex(self) -> Pattern:
        return self._inexact_number_unit_regex

    @property
    def suffix_and_regex(self) -> Pattern:
        return self._suffix_and_regex

    @property
    def relative_duration_unit_regex(self) -> Pattern:
        return self._relative_duration_unit_regex

    @property
    def more_than_regex(self) -> Pattern:
        return self._more_than_regex

    @property
    def less_than_regex(self) -> Pattern:
        return self._less_than_regex

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def during_regex(self) -> Pattern:
        return self._during_regex

    @property
    def unit_map(self) -> Pattern:
        return self._unit_map

    @property
    def unit_value_map(self) -> {}:
        return self._unit_value_map

    @property
    def duration_unit_regex(self) -> {}:
        return self._duration_unit_regex

    @property
    def duration_connector_regex(self) -> Pattern:
        return self._duration_connector_regex

    def __init__(self):
        super().__init__()
        self._check_both_before_after = PortugueseDateTime.CheckBothBeforeAfter
        self._all_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.AllRegex)
        self._half_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.HalfRegex)
        self._followed_unit: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.FollowedUnit)
        self._number_combined_with_unit: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.DurationNumberCombinedWithUnit)
        self._an_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.AnUnitRegex)
        self._inexact_number_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.InexactNumberUnitRegex)
        self._suffix_and_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.SuffixAndRegex)
        self._relative_duration_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.RelativeDurationUnitRegex
        )
        self._during_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.DuringRegex
        )
        self._cardinal_extractor: BaseNumberExtractor = PortugueseCardinalExtractor()
        self._unit_map = PortugueseDateTime.UnitMap
        self._unit_value_map = PortugueseDateTime.UnitValueMap
        self._duration_unit_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.DurationUnitRegex
        )
        self._duration_connector_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.DurationConnectorRegex
        )
        self._more_than_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.MoreThanRegex
        )
        self._less_than_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.LessThanRegex
        )
        self._conjunction_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.ConjunctionRegex
        )
        self._inexact_number_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.InexactNumberRegex
        )
        self._special_number_with_unit_regex = None
        self._check_both_before_after = PortugueseDateTime.CheckBothBeforeAfter
        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._special_number_unit_regex = None
