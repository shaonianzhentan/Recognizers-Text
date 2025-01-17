#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List

from ms_recognizers_text.utilities import RegExpUtility
from ms_recognizers_text.culture import Culture
from ms_recognizers_text.parser import ParseResult
from ms_recognizers_number.culture import CultureInfo
from ms_recognizers_number.number.parsers import NumberParserConfiguration
from ms_recognizers_number.resources.german_numeric import GermanNumeric


class GermanNumberParserConfiguration(NumberParserConfiguration):
    @property
    def cardinal_number_map(self) -> Dict[str, int]:
        return self._cardinal_number_map

    @property
    def ordinal_number_map(self) -> Dict[str, int]:
        return self._ordinal_number_map

    @property
    def round_number_map(self) -> Dict[str, int]:
        return self._round_number_map

    @property
    def culture_info(self):
        return self._culture_info

    @property
    def digital_number_regex(self) -> Pattern:
        return self._digital_number_regex

    @property
    def fraction_marker_token(self) -> str:
        return self._fraction_marker_token

    @property
    def negative_number_sign_regex(self) -> Pattern:
        return self._negative_number_sign_regex

    @property
    def half_a_dozen_regex(self) -> Pattern:
        return self._half_a_dozen_regex

    @property
    def half_a_dozen_text(self) -> str:
        return self._half_a_dozen_text

    @property
    def lang_marker(self) -> str:
        return self._lang_marker

    @property
    def non_decimal_separator_char(self) -> str:
        return self._non_decimal_separator_char

    @property
    def decimal_separator_char(self) -> str:
        return self._decimal_separator_char

    @property
    def word_separator_token(self) -> str:
        return self._word_separator_token

    @property
    def written_decimal_separator_texts(self) -> List[str]:
        return self._written_decimal_separator_texts

    @property
    def written_group_separator_texts(self) -> List[str]:
        return self._written_group_separator_texts

    @property
    def written_integer_separator_texts(self) -> List[str]:
        return self._written_integer_separator_texts

    @property
    def written_fraction_separator_texts(self) -> List[str]:
        return self._written_fraction_separator_texts

    @property
    def non_standard_separator_variants(self) -> List[str]:
        return self._non_standard_separator_variants

    @property
    def is_multi_decimal_separator_culture(self) -> bool:
        return self._is_multi_decimal_separator_culture

    @property
    def round_multiplier_regex(self) -> Pattern:
        return self._round_multiplier_regex

    def __init__(self, culture_info=None):
        if culture_info is None:
            culture_info = CultureInfo(Culture.German)

        self._culture_info = culture_info
        self._lang_marker = GermanNumeric.LangMarker
        self._decimal_separator_char = GermanNumeric.DecimalSeparatorChar
        self._fraction_marker_token = GermanNumeric.FractionMarkerToken
        self._non_decimal_separator_char = GermanNumeric.NonDecimalSeparatorChar
        self._half_a_dozen_text = GermanNumeric.HalfADozenText
        self._word_separator_token = GermanNumeric.WordSeparatorToken
        self._non_standard_separator_variants = []
        self._is_multi_decimal_separator_culture = GermanNumeric.MultiDecimalSeparatorCulture

        self._written_decimal_separator_texts = GermanNumeric.WrittenDecimalSeparatorTexts
        self._written_group_separator_texts = GermanNumeric.WrittenGroupSeparatorTexts
        self._written_integer_separator_texts = GermanNumeric.WrittenIntegerSeparatorTexts
        self._written_fraction_separator_texts = GermanNumeric.WrittenFractionSeparatorTexts

        self._cardinal_number_map = GermanNumeric.CardinalNumberMap
        self._ordinal_number_map = GermanNumeric.OrdinalNumberMap
        self._round_number_map = GermanNumeric.RoundNumberMap
        self._negative_number_sign_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.NegativeNumberSignRegex)
        self._half_a_dozen_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.HalfADozenRegex)
        self._digital_number_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.DigitalNumberRegex)
        self._round_multiplier_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.RoundMultiplierRegex)
        self._fraction_units_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.FractionUnitsRegex)
        self._fraction_half_regex = RegExpUtility.get_safe_reg_exp(
            GermanNumeric.FractionHalfRegex)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = list()
        tokens_len = len(tokens)
        i = 0
        while i < tokens_len:
            if '-' in tokens[i]:
                splited_tokens = tokens[i].split('-')
                if len(splited_tokens) == 2 and splited_tokens[1] in self.ordinal_number_map:
                    frac_words.append(splited_tokens[0])
                    frac_words.append(splited_tokens[1])
                else:
                    frac_words.append(tokens[i])
            elif i < tokens_len - 2 and tokens[i + 1] == '-':
                if tokens[i + 2] in self.ordinal_number_map:
                    frac_words.append(tokens[i])
                    frac_words.append(tokens[i + 2])
                else:
                    frac_words.append(
                        tokens[i] + tokens[i + 1] + tokens[i + 2])
                i += 2
            else:
                frac_words.append(tokens[i])
            i += 1

        # The following piece of code is needed to compute the fraction pattern number+'einhalb'
        # e.g. 'zweieinhalb' ('two and a half').
        try:
            frac_words.remove("/")  # .remove() raises a value error so this must be caught
        except ValueError:
            pass
        for idx, word in enumerate(frac_words):
            if self._fraction_half_regex.search(word):  # zweieinhalb, dreienhalb etc. case
                frac_words[idx] = word[0:(len(word)-7)]
                frac_words.append(self._written_fraction_separator_texts[0])
                frac_words.append(GermanNumeric.OneHalfTokens[0])
                frac_words.append(GermanNumeric.OneHalfTokens[1])
            elif self._fraction_units_regex.search(word):
                m = self._fraction_units_regex.search(word)
                if m.group("onehalf"):  # 'einundhalb' case
                    frac_words[idx] = GermanNumeric.OneHalfTokens[0]
                    frac_words.append(self._written_fraction_separator_texts[0])
                    frac_words.append(GermanNumeric.OneHalfTokens[0])
                    frac_words.append(GermanNumeric.OneHalfTokens[1])
                if m.group("quarter"):  # 'dreiviertal' case
                    frac_words[idx] = word[0:len("drei")]
                    frac_words.append(self._written_fraction_separator_texts[0])
                    frac_words.append(word[len(frac_words[idx]):len("viertel")+len(frac_words[idx])])

        return frac_words

    def resolve_composite_number(self, number_str: str) -> int:
        if '-' in number_str:
            numbers = number_str.split('-')
            ret = 0
            for num in numbers:
                if num in self.ordinal_number_map:
                    ret += self.ordinal_number_map[num]
                elif num in self.cardinal_number_map:
                    ret += self.cardinal_number_map[num]
            return ret
        elif number_str in self.ordinal_number_map:
            return self.ordinal_number_map[number_str]
        elif number_str in self.cardinal_number_map:
            return self.cardinal_number_map[number_str]

        return 0
