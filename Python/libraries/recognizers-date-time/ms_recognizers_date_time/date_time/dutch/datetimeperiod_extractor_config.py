#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from ms_recognizers_number import BaseNumberExtractor, DutchCardinalExtractor
from ms_recognizers_text.utilities import RegExpUtility
from ...resources.dutch_date_time import DutchDateTime
from ..extractors import DateTimeExtractor
from ..base_datetimeperiod import DateTimePeriodExtractorConfiguration, MatchedIndex
from ..base_date import BaseDateExtractor
from ..base_time import BaseTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_timeperiod import BaseTimePeriodExtractor
from ..base_datetime import BaseDateTimeExtractor
from ..base_timezone import BaseTimeZoneExtractor
from .date_extractor_config import DutchDateExtractorConfiguration
from .time_extractor_config import DutchTimeExtractorConfiguration
from .duration_extractor_config import DutchDurationExtractorConfiguration
from .timeperiod_extractor_config import DutchTimePeriodExtractorConfiguration
from .timezone_extractor_config import DutchTimeZoneExtractorConfiguration
from .datetime_extractor_config import DutchDateTimeExtractorConfiguration


class DutchDateTimePeriodExtractorConfiguration(DateTimePeriodExtractorConfiguration):
    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def suffix_regex(self) -> Pattern:
        return self._suffix_regex

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def single_date_extractor(self) -> DateTimeExtractor:
        return self._single_date_extractor

    @property
    def single_time_extractor(self) -> DateTimeExtractor:
        return self._single_time_extractor

    @property
    def single_date_time_extractor(self) -> DateTimeExtractor:
        return self._single_date_time_extractor

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def time_period_extractor(self) -> DateTimeExtractor:
        return self._time_period_extractor

    @property
    def time_zone_extractor(self) -> DateTimeExtractor:
        return self._time_zone_extractor

    @property
    def simple_cases_regexes(self) -> List[Pattern]:
        return self._simple_cases_regexes

    @property
    def preposition_regex(self) -> Pattern:
        return self._preposition_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def specific_time_of_day_regex(self) -> Pattern:
        return self._specific_time_of_day_regex

    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def period_time_of_day_with_date_regex(self) -> Pattern:
        return self._period_time_of_day_with_date_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def time_unit_regex(self) -> Pattern:
        return self._time_unit_regex

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._past_prefix_regex

    @property
    def next_prefix_regex(self) -> Pattern:
        return self._next_prefix_regex

    @property
    def relative_time_unit_regex(self) -> Pattern:
        return self._relative_time_unit_regex

    @property
    def rest_of_date_time_regex(self) -> Pattern:
        return self._rest_of_date_time_regex

    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def general_ending_regex(self) -> Pattern:
        return self._general_ending_regex

    @property
    def middle_pause_regex(self) -> Pattern:
        return self._middle_pause_regex

    @property
    def within_next_prefix_regex(self) -> Pattern:
        return self._within_next_prefix_regex

    @property
    def token_before_date(self) -> str:
        return self._token_before_date

    @property
    def future_suffix_regex(self) -> Pattern:
        return self._future_suffix_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def am_desc_regex(self) -> Pattern:
        return self._am_desc_regex

    @property
    def pm_desc_regex(self) -> Pattern:
        return self._pm_desc_regex

    @property
    def prefix_day_regex(self) -> Pattern:
        return self._prefix_day_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    def __init__(self):
        super().__init__()
        self._check_both_before_after = DutchDateTime.CheckBothBeforeAfter
        self._simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.PureNumFromTo),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.TimeDateFromTo),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.PureNumBetweenAnd),
            RegExpUtility.get_safe_reg_exp(
                DutchDateTime.SpecificTimeOfDayRegex)
        ]

        self._preposition_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PrepositionRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TillRegex)
        self._specific_time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.SpecificTimeOfDayRegex)
        self._time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PeriodTimeOfDayRegex)
        self._followed_unit = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TimeFollowedUnit)
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TimeUnitRegex)
        self._past_prefix_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PastSuffixRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.NextPrefixRegex)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TimeNumberCombinedWithUnit)
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.WeekDayRegex)
        self._period_time_of_day_with_date_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PeriodTimeOfDayWithDateRegex)
        self._relative_time_unit_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.RelativeTimeUnitRegex)
        self._rest_of_date_time_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.RestOfDateTimeRegex)
        self._general_ending_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.GeneralEndingRegex)
        self._middle_pause_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.MiddlePauseRegex)

        self.from_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.FromRegex)
        self.range_connector_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.RangeConnectorRegex)

        self._cardinal_extractor = DutchCardinalExtractor()

        self._single_date_extractor = BaseDateExtractor(
            DutchDateExtractorConfiguration())
        self._single_time_extractor = BaseTimeExtractor(
            DutchTimeExtractorConfiguration())
        self._single_date_time_extractor = BaseDateTimeExtractor(
            DutchDateTimeExtractorConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            DutchDurationExtractorConfiguration())
        self._time_period_extractor = BaseTimePeriodExtractor(
            DutchTimePeriodExtractorConfiguration())
        self._time_zone_extractor = BaseTimeZoneExtractor(
            DutchTimeZoneExtractorConfiguration())
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.WithinNextPrefixRegex
        )
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.TimeUnitRegex
        )
        self._token_before_date = DutchDateTime.TokenBeforeDate
        self._future_suffix_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.FutureSuffixRegex
        )
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.DateUnitRegex
        )
        self._am_desc_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.AmDescRegex
        )
        self._pm_desc_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PmDescRegex
        )
        self._prefix_day_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.PrefixDayRegex
        )
        self._before_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.BeforeRegex
        )
        self._after_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.AfterRegex
        )
        self._suffix_regex = RegExpUtility.get_safe_reg_exp(
            DutchDateTime.SuffixRegex
        )
        self._check_both_before_after = DutchDateTime.CheckBothBeforeAfter

    def get_from_token_index(self, source: str) -> MatchedIndex:
        match = self.from_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        match = self.before_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        match = self.range_connector_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)
