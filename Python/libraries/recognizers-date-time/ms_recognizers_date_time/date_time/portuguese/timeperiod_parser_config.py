#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, Dict

from ms_recognizers_text.utilities import RegExpUtility
from ms_recognizers_text.extractor import Extractor
from ms_recognizers_number.number.portuguese.extractors import PortugueseIntegerExtractor
from ...resources.portuguese_date_time import PortugueseDateTime
from ..extractors import DateTimeExtractor
from ..parsers import DateTimeParser
from ..base_configs import BaseDateParserConfiguration, DateTimeUtilityConfiguration
from ..base_timeperiod import TimePeriodParserConfiguration, MatchedTimeRegex
from ..utilities import TimexUtil
from ..constants import Constants


class PortugueseTimePeriodParserConfiguration(TimePeriodParserConfiguration):
    @property
    def time_extractor(self) -> DateTimeExtractor:
        return self._time_extractor

    @property
    def time_parser(self) -> DateTimeParser:
        return self._time_parser

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

    @property
    def pure_number_from_to_regex(self) -> Pattern:
        return self._pure_number_from_to_regex

    @property
    def pure_number_between_and_regex(self) -> Pattern:
        return self._pure_number_between_and_regex

    @property
    def specific_time_from_to_regex(self) -> Pattern:
        return self._specific_time_from_to_regex

    @property
    def specific_time_between_and_regex(self) -> Pattern:
        return self._specific_time_between_and_regex

    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def numbers(self) -> Dict[str, int]:
        return self._numbers

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    def __init__(self, config: BaseDateParserConfiguration):
        self._time_extractor = config.time_extractor
        self._time_parser = config.time_parser
        self._time_zone_parser = config.time_zone_parser
        self._integer_extractor = PortugueseIntegerExtractor()
        self._pure_number_from_to_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.PureNumFromTo)
        self._pure_number_between_and_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.PureNumBetweenAnd)
        self._specific_time_from_to_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.SpecificTimeFromTo)
        self._specific_time_between_and_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.SpecificTimeBetweenAnd)
        self._time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.TimeOfDayRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.TillRegex)
        self._numbers = PortugueseDateTime.Numbers
        self._utility_configuration = config.utility_configuration

    def get_matched_timex_range(self, source: str) -> MatchedTimeRegex:
        trimmed_text = source.strip().lower()
        if trimmed_text.endswith('s'):
            trimmed_text = trimmed_text[:-1]

        timex = ''
        begin_hour = 0
        end_hour = 0
        end_min = 0

        time_of_day = ""
        if any(trimmed_text.endswith(o) for o in PortugueseDateTime.MorningTermList):
            time_of_day = Constants.MORNING
        elif any(trimmed_text.endswith(o) for o in PortugueseDateTime.AfternoonTermList):
            time_of_day = Constants.AFTERNOON
        elif any(trimmed_text.endswith(o) for o in PortugueseDateTime.EveningTermList):
            time_of_day = Constants.EVENING
        elif any(trimmed_text == o for o in PortugueseDateTime.DaytimeTermList):
            time_of_day = Constants.DAYTIME
        elif any(trimmed_text.endswith(o) for o in PortugueseDateTime.NightTermList):
            time_of_day = Constants.NIGHT
        else:
            return MatchedTimeRegex(
                matched=False,
                timex='',
                begin_hour=0,
                end_hour=0,
                end_min=0
            )

        parse_result = TimexUtil.parse_time_of_day(time_of_day)
        timex = parse_result.timex
        begin_hour = parse_result.begin_hour
        end_hour = parse_result.end_hour
        end_min = parse_result.end_min

        return MatchedTimeRegex(
            matched=True,
            timex=timex,
            begin_hour=begin_hour,
            end_hour=end_hour,
            end_min=end_min
        )
