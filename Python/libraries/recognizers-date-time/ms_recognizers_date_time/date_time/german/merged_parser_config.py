#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern

from ms_recognizers_text.utilities import RegExpUtility

from .holiday_parser_config import GermanHolidayParserConfiguration
from .set_parser_config import GermanSetParserConfiguration
from .dateperiod_parser_config import GermanDatePeriodParserConfiguration
from .timeperiod_parser_config import GermanTimePeriodParserConfiguration
from .common_configs import GermanCommonDateTimeParserConfiguration
from ..base_date import BaseDateParser
from ..base_time import BaseTimeParser
from ..base_datetime import BaseDateTimeParser
from ..base_holiday import BaseHolidayParser
from ..base_dateperiod import BaseDatePeriodParser
from ..base_timeperiod import BaseTimePeriodParser
from ..base_datetimeperiod import BaseDateTimePeriodParser
from ..base_duration import BaseDurationParser
from ..base_set import BaseSetParser
from ..base_merged import MergedParserConfiguration
from ...resources.german_date_time import GermanDateTime, BaseDateTime


class GermanMergedParserConfiguration(GermanCommonDateTimeParserConfiguration, MergedParserConfiguration):
    @property
    def around_regex(self) -> Pattern:
        return self._around_regex

    @property
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def suffix_after(self) -> Pattern:
        return self._suffix_after

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    @property
    def since_regex(self) -> Pattern:
        return self._since_regex

    @property
    def date_parser(self) -> BaseDateParser:
        return self._date_parser

    @property
    def holiday_parser(self) -> BaseHolidayParser:
        return self._holiday_parser

    @property
    def time_parser(self) -> BaseTimeParser:
        return self._time_parser

    @property
    def date_time_parser(self) -> BaseDateTimeParser:
        return self._date_time_parser

    @property
    def date_period_parser(self) -> BaseDatePeriodParser:
        return self._date_period_parser

    @property
    def time_period_parser(self) -> BaseTimePeriodParser:
        return self._time_period_parser

    @property
    def date_time_period_parser(self) -> BaseDateTimePeriodParser:
        return self._date_time_period_parser

    @property
    def duration_parser(self) -> BaseDurationParser:
        return self._duration_parser

    @property
    def set_parser(self) -> BaseSetParser:
        return self._set_parser

    def __init__(self, config):
        GermanCommonDateTimeParserConfiguration.__init__(self)
        self._suffix_after = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.SuffixAfterRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(GermanDateTime.YearRegex)
        self._equal_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.EqualRegex)
        self._around_regex = RegExpUtility.get_safe_reg_exp(GermanDateTime.AroundRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.BeforeRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.AfterRegex)
        self._since_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.SinceRegex)

        self._date_period_parser = BaseDatePeriodParser(
            GermanDatePeriodParserConfiguration(self))
        self._time_period_parser = BaseTimePeriodParser(
            GermanTimePeriodParserConfiguration(self))
        self._set_parser = BaseSetParser(GermanSetParserConfiguration(config))
        self._holiday_parser = BaseHolidayParser(
            GermanHolidayParserConfiguration(config))
