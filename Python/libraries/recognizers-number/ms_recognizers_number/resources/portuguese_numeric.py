# ------------------------------------------------------------------------------
# <auto-generated>
#     This code was generated by a tool.
#     Changes to this file may cause incorrect behavior and will be lost if
#     the code is regenerated.
# </auto-generated>
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ------------------------------------------------------------------------------

from .base_numbers import BaseNumbers
# pylint: disable=line-too-long


class PortugueseNumeric:
    LangMarker = 'Por'
    CompoundNumberLanguage = False
    MultiDecimalSeparatorCulture = False
    HundredsNumberIntegerRegex = f'(quatrocent[ao]s|trezent[ao]s|seiscent[ao]s|setecent[ao]s|oitocent[ao]s|novecent[ao]s|duzent[ao]s|quinhent[ao]s|cem|(?<!por\\s+)(cento))'
    RoundNumberIntegerRegex = f'(mil(h([ãa]o|[õo]es))?|bilh([ãa]o|[õo]es)|trilh([ãa]o|[õo]es)|qua[td]rilh([ãa]o|[õo]es)|quintilh([ãa]o|[õo]es))'
    ZeroToNineIntegerRegex = f'(quatro|cinco|sete|nove|zero|tr[êe]s|seis|oito|d(oi|ua)s|h?uma?)'
    TwoToNineIntegerRegex = f'(quatro|cinco|sete|nove|tr[êe]s|seis|oito|d(oi|ua)s)'
    TenToNineteenIntegerRegex = f'(dez[ea]sseis|dez[ea]ssete|dez[ea]nove|dezoito|(c|qua)torze|quinze|treze|d[ée]z|onze|doze)'
    TensNumberIntegerRegex = f'(cinquenta|quarenta|trinta|sessenta|setenta|oitenta|noventa|vinte)'
    DigitsNumberRegex = f'\\d|\\d{{1,3}}(\\.\\d{{3}})'
    BelowHundredsRegex = f'(({TenToNineteenIntegerRegex}|({TensNumberIntegerRegex}(\\s+e\\s+{ZeroToNineIntegerRegex})?))|{ZeroToNineIntegerRegex})'
    BelowThousandsRegex = f'({HundredsNumberIntegerRegex}(\\s+e\\s+{BelowHundredsRegex})?|{BelowHundredsRegex})'
    SupportThousandsRegex = f'(({BelowThousandsRegex}|{BelowHundredsRegex})\\s+{RoundNumberIntegerRegex}(\\s+{RoundNumberIntegerRegex})?)'
    NegativeNumberTermsRegex = f'^[.]'
    NegativeNumberSignRegex = f'^({NegativeNumberTermsRegex}\\s+).*'
    SeparaIntRegex = f'({SupportThousandsRegex}(\\s+{SupportThousandsRegex})*(\\s+{BelowThousandsRegex})?|{BelowThousandsRegex})'
    AllIntRegex = f'({SeparaIntRegex}|mil(\\s+{BelowThousandsRegex})?)'
    AllPointRegex = f'((\\s+{ZeroToNineIntegerRegex})+|(\\s+{AllIntRegex}))'
    SpecialFractionInteger = f'((({AllIntRegex})i?({ZeroToNineIntegerRegex})|({AllIntRegex}))\\s+a?v[oa]s?)'
    PlaceHolderDefault = f'\\D|\\b'
    PlaceHolderPureNumber = f'\\b'
    AllIntRegexWithLocks = f'((?<=\\b){AllIntRegex}(?=\\b))'
    AllIntRegexWithDozenSuffixLocks = f'(?<=\\b)(((meia)?\\s+(d[úu]zia))|({AllIntRegex}\\s+(e|com)\\s+)?({AllIntRegex}\\s+(d[úu]zia(s)?|dezena(s)?)))(?=\\b)'

    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+(?!(,\\d+[a-zA-Z]))(?={placeholder})'
    NumbersWithSuffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    RoundNumberIntegerRegexWithLocks = f'(?<=\\b)({DigitsNumberRegex})+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    NumbersWithDozenSuffix = f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+\\s+dezena(s)?(?=\\b)'
    NumbersWithDozen2Suffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+d[úu]zia(s)(?=\\b)'
    SimpleRoundOrdinalRegex = f'(mil[eé]sim[oa]|milion[eé]sim[oa]|bilion[eé]sim[oa]|trilion[eé]sim[oa]|quatrilion[eé]sim[oa]|quintilion[eé]sim[oa])'
    OneToNineOrdinalRegex = f'(primeir[oa]|segund[oa]|terceir[oa]|terç[oa]|quart[oa]|quint[oa]|sext[oa]|s[eé]tim[oa]|oitav[oa]|non[oa])'
    TensOrdinalRegex = f'(nonag[eé]sim[oa]|octog[eé]sim[oa]|setuag[eé]sim[oa]|septuag[eé]sim[oa]|sexag[eé]sim[oa]|quinquag[eé]sim[oa]|quadrag[eé]sim[oa]|trig[eé]sim[oa]|vig[eé]sim[oa]|d[eé]cim[oa])'
    HundredOrdinalRegex = f'(cent[eé]sim[oa]|ducent[eé]sim[oa]|tricent[eé]sim[oa]|cuadringent[eé]sim[oa]|quingent[eé]sim[oa]|sexcent[eé]sim[oa]|septingent[eé]sim[oa]|octingent[eé]sim[oa]|noningent[eé]sim[oa])'
    SpecialUnderHundredOrdinalRegex = f'(und[eé]cim[oa]|duod[eé]cimo)'
    UnderHundredOrdinalRegex = f'((({TensOrdinalRegex}(\\s)?)?{OneToNineOrdinalRegex})|{TensOrdinalRegex}|{SpecialUnderHundredOrdinalRegex})'
    UnderThousandOrdinalRegex = f'((({HundredOrdinalRegex}(\\s)?)?{UnderHundredOrdinalRegex})|{HundredOrdinalRegex})'
    OverThousandOrdinalRegex = f'(({AllIntRegex})([eé]sim[oa]))'
    RelativeOrdinalRegex = f'(?<relativeOrdinal>pr[oó]xim[ao]s?|[uú]ltim[ao]\\s+mas\\s+um|anterior\\s+ao\\s+últim[ao]|(pen)?[uú]ltim[ao]s?|antepen[uú]ltim[ao]s?|seguintes?|anterior(es)?|atua(l|is))'
    ComplexOrdinalRegex = f'(({OverThousandOrdinalRegex}(\\s)?)?{UnderThousandOrdinalRegex}|{OverThousandOrdinalRegex})'
    SuffixRoundOrdinalRegex = f'(({AllIntRegex})({SimpleRoundOrdinalRegex}))'
    ComplexRoundOrdinalRegex = f'((({SuffixRoundOrdinalRegex}(\\s)?)?{ComplexOrdinalRegex})|{SuffixRoundOrdinalRegex})'
    AllOrdinalNumberRegex = f'{ComplexOrdinalRegex}|{SimpleRoundOrdinalRegex}|{ComplexRoundOrdinalRegex}'
    AllOrdinalRegex = f'(?:{AllOrdinalNumberRegex}|{RelativeOrdinalRegex})'
    OrdinalSuffixRegex = f'(?<=\\b)(\\d*((1|2|3|4|5|6|7|8|9|0)[oaºª]|(1|2|3|4|5|6|7|8|9)(\\.[ºª])))(?=\\b)'
    OrdinalEnglishRegex = f'(?<=\\b){AllOrdinalRegex}(?=\\b)'
    FractionNotationRegex = f'{BaseNumbers.FractionNotationRegex}'
    FractionNotationWithSpacesRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    FractionMultiplierRegex = f'(?<fracMultiplier>\\s+(e|com)\\s+(meio|(um|{TwoToNineIntegerRegex})\\s+(meio|terç[oa]|quart[oa]|quint[oa]|sext[oa]|s[eé]tim[oa]|oitav[oa]|non[oa]|d[eé]cim[oa])s?))'
    RoundMultiplierWithFraction = f'(?<multiplier>(?:(mil(h([ãa]o|[õo]es))|bilh([ãa]o|[õo]es)|trilh([ãa]o|[õo]es)|qua[td]rilh([ãa]o|[õo]es)|quintilh([ãa]o|[õo]es))))(?={FractionMultiplierRegex}?$)'
    RoundMultiplierRegex = f'\\b\\s*({RoundMultiplierWithFraction}|(?<multiplier>(mil))$)'
    FractionNounRegex = f'(?<=\\b)({AllIntRegex}\\s+((e|com)\\s+)?)?(({AllIntRegex})(\\s+((e|com)\\s)?)((({AllOrdinalNumberRegex})s?|({SpecialFractionInteger})|({SuffixRoundOrdinalRegex})s?)|mei[oa]?|ter[çc]o?)|(meio|um\\s+quarto\\s+de)\\s+{RoundNumberIntegerRegex})(?=\\b)'
    FractionNounWithArticleRegex = f'(?<=\\b)(({AllIntRegex}|{RoundNumberIntegerRegexWithLocks})\\s+(e\\s+)?)?((um|um[as])(\\s+)(({AllOrdinalNumberRegex})|({SuffixRoundOrdinalRegex})|(e\\s+)?mei[oa]?)|mei[oa]?)(?=\\b)'
    FractionPrepositionRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<!\\.)\\d+))\\s+sobre\\s+(?<denominator>({AllIntRegex})|((\\d+)(?!\\.)))(?=\\b)'
    AllFloatRegex = f'(?<!(entre\\s+(menos\\+)?)){AllIntRegex}(\\s+(v[íi]rgula|e|ponto)){AllPointRegex}'
    DoubleWithMultiplierRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\,)))\\d+,\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    DoubleExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))(\\d+(,\\d+)?)e([+-]*[1-9]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))(\\d+(,\\d+)?)\\^([+-]*[1-9]\\d*)(?=\\b)'

    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))\\d+,\\d+(?!(,\\d+))(?={placeholder})'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+)),\\d+(?!(,\\d+))(?={placeholder})'
    DoubleWithRoundNumber = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\,)))\\d+,\\d+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    DoubleAllFloatRegex = f'((?<=\\b){AllFloatRegex}(?=\\b))'
    NumberWithSuffixPercentage = f'(?<!%)({BaseNumbers.NumberReplaceToken})(\\s*)(%(?!{BaseNumbers.NumberReplaceToken})|(por cento|pontos percentuais)\\b)'
    TillRegex = f'(\\b[aà]\\b|at[eé]h?|--|-|—|——|~|–)'
    MoreRegex = f'(mais\\s+(alt[oa]s?|grandes?)\\s+que|(mais|maior(es)?|superior(es)?|acima)\\b((\\s+(que|de|a))|(?=\\s+ou\\b))|(?<!<|=)>)'
    LessRegex = f'(mais\\s+baix[oa]\\s+que|(meno(s|r(es)?)|inferior(es)?|abaixo)(\\s+(que|de|a)|(?=\\s+ou\\b))|(?<!>|=)<)'
    EqualRegex = f'((igua(l|is)|equivalente(s)?|equivale(ndo)?)(\\s+(ao?|que|d[eao]))?|(?<!<|>)=)'
    MoreOrEqualPrefix = f'((n[ãa]o\\s+{LessRegex})|((pelo|ao)\\s+menos|(como(\\s+o)?|no)\\s+m[íi]nimo))'
    MoreOrEqual = f'(({MoreRegex}\\s+(ou)?\\s+{EqualRegex})|({EqualRegex}\\s+(ou|e)\\s+{MoreRegex})|{MoreOrEqualPrefix}(\\s+(ou)\\s+{EqualRegex})?|({EqualRegex}\\s+(ou)\\s+)?{MoreOrEqualPrefix}|>\\s*=)'
    MoreOrEqualSuffix = f'((\\b(e|ou)\\b\\s+(mais|maior(es)?|superior(es)?)((?!\\s+(alt[oa]|baix[oa]|que|d[eao]|ao?))|(\\s+(que|d[eao]|ao?)(?!(\\s*\\d+)))))|(como(\\s+o)?|no)\\s+m[íi]nimo|(pelo|ao)\\s+menos)\\b'
    LessOrEqualPrefix = f'((n[ãa]o\\s+{MoreRegex})|((como(\\s+o)?|no)\\s+m[aá]ximo))'
    LessOrEqual = f'(({LessRegex}\\s+(ou)?\\s+{EqualRegex})|({EqualRegex}\\s+(ou)?\\s+{LessRegex})|{LessOrEqualPrefix}(\\s+(ou)?\\s+{EqualRegex})?|({EqualRegex}\\s+(ou)?\\s+)?{LessOrEqualPrefix}|<\\s*=)'
    LessOrEqualSuffix = f'((\\b(e|ou)\\b\\s+(meno(s|r(es)?|inferior(es)?))((?!\\s+(alt[oa]|baix[oa]|que|d[eao]|ao?))|(\\s+(que|d[eao]|ao?)(?!(\\s*\\d+)))))|(como(\\s+o)?|no)\\s+m[áa]ximo)\\b'
    NumberSplitMark = f'(?![,.](?!\\d+))(?!\\s*\\b(((e)\\s+)?({LessRegex}|{MoreRegex}|{EqualRegex}|n[ãa]o|d[eao])|mas|[ao])\\b)'
    MoreRegexNoNumberSucceed = f'(\\b(mais|maior(es)?|superior(es)?)((?!\\s+(que|d[eao]|ao?))|\\s+((que|d[eao])(?!(\\s*\\d+))))|((por\\s+|a)cima)(?!(\\s*\\d+)))\\b'
    LessRegexNoNumberSucceed = f'(\\b(meno(s|r(es)?)|inferior(es)?)((?!\\s+(que|d[eao]|ao?))|\\s+((que|d[eao]|ao?)(?!(\\s*\\d+))))|((por\\s+|a)baixo)(?!(\\s*\\d+)))\\b'
    EqualRegexNoNumberSucceed = f'(\\b(igua(l|is)|equivalentes?|equivale(ndo)?)((?!\\s+(ao?|que|d[eao]))|(\\s+(ao?|que|d[eao])(?!(\\s*\\d+)))))\\b'
    OneNumberRangeMoreRegex1 = f'({MoreOrEqual}|{MoreRegex})\\s*(([ao]s?)\\s+)?(?<number1>({NumberSplitMark}.)+)'
    OneNumberRangeMoreRegex1LB = f'(?<!n[ãa]o\\s+){OneNumberRangeMoreRegex1}'
    OneNumberRangeMoreRegex2 = f'(?<number1>({NumberSplitMark}.)+)\\s*{MoreOrEqualSuffix}'
    OneNumberRangeMoreSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+ou\\s+){MoreRegexNoNumberSucceed})|({MoreRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+ou\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeLessRegex1 = f'({LessOrEqual}|{LessRegex})\\s*([ao]s?\\s+)?(?<number2>({NumberSplitMark}.)+)'
    OneNumberRangeLessRegex1LB = f'(?<!n[ãa]o\\s+){OneNumberRangeLessRegex1}'
    OneNumberRangeLessRegex2 = f'(?<number2>({NumberSplitMark}.)+)\\s*{LessOrEqualSuffix}'
    OneNumberRangeLessSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+ou\\s+){LessRegexNoNumberSucceed})|({LessRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+ou\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeEqualRegex = f'{EqualRegex}\\s*([ao]s?\\s+)?(?<number1>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex1 = f'\\bentre\\s*([ao]s?\\s+)?(?<number1>({NumberSplitMark}.)+)\\s*e\\s*([ao]s?\\s+)?(?<number2>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex2 = f'({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})\\s*(\\be\\b|mas|,)\\s*({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})'
    TwoNumberRangeRegex3 = f'({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})\\s*(\\be\\b|mas|,)\\s*({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})'
    TwoNumberRangeRegex4 = f'(\\bde(sde)?\\s+)?(\\b[ao]s?\\s+)?\\b(?!\\s+)(?<number1>({NumberSplitMark}(?!\\b(entre|de(sde)?|es)\\b).)+)\\b\\s*{TillRegex}\\s*([ao]s?\\s+)?\\b(?!\\s+)(?<number2>({NumberSplitMark}.)+)\\b'
    AmbiguousFractionConnectorsRegex = f'(\\b(em|de)\\b)'
    DecimalSeparatorChar = ','
    FractionMarkerToken = 'sobre'
    NonDecimalSeparatorChar = '.'
    HalfADozenText = 'seis'
    WordSeparatorToken = 'e'
    WrittenDecimalSeparatorTexts = [r'virgula', r'vírgula']
    WrittenGroupSeparatorTexts = [r'ponto']
    WrittenIntegerSeparatorTexts = [r'e']
    WrittenFractionSeparatorTexts = [r'com']
    WrittenFractionSuffix = [r'avo', r'ava']
    OneHalfTokens = [r'um', r'meio']
    PluralSuffix = 's'
    HalfADozenRegex = f'meia\\s+d[uú]zia'
    DigitalNumberRegex = f'((?<=\\b)(mil(hares)?|ce(m|ntenas?)|[bmt]ilh([aã]o|[oõ]es)|dezenas?)(?=\\b))|((?<=(\\d|\\b)){BaseNumbers.MultiplierLookupRegex}(?=\\b))'
    CardinalNumberMap = dict([("zero", 0),
                              ("hum", 1),
                              ("um", 1),
                              ("uma", 1),
                              ("dois", 2),
                              ("duas", 2),
                              ("meia", 2),
                              ("meio", 2),
                              ("tres", 3),
                              ("três", 3),
                              ("quatro", 4),
                              ("cinco", 5),
                              ("seis", 6),
                              ("sete", 7),
                              ("oito", 8),
                              ("nove", 9),
                              ("dez", 10),
                              ("dezena", 10),
                              ("déz", 10),
                              ("onze", 11),
                              ("doze", 12),
                              ("dúzia", 12),
                              ("duzia", 12),
                              ("dúzias", 12),
                              ("duzias", 12),
                              ("treze", 13),
                              ("catorze", 14),
                              ("quatorze", 14),
                              ("quinze", 15),
                              ("dezesseis", 16),
                              ("dezasseis", 16),
                              ("dezessete", 17),
                              ("dezassete", 17),
                              ("dezoito", 18),
                              ("dezenove", 19),
                              ("dezanove", 19),
                              ("vinte", 20),
                              ("trinta", 30),
                              ("quarenta", 40),
                              ("cinquenta", 50),
                              ("cincoenta", 50),
                              ("sessenta", 60),
                              ("setenta", 70),
                              ("oitenta", 80),
                              ("noventa", 90),
                              ("cem", 100),
                              ("cento", 100),
                              ("duzentos", 200),
                              ("duzentas", 200),
                              ("trezentos", 300),
                              ("trezentas", 300),
                              ("quatrocentos", 400),
                              ("quatrocentas", 400),
                              ("quinhentos", 500),
                              ("quinhentas", 500),
                              ("seiscentos", 600),
                              ("seiscentas", 600),
                              ("setecentos", 700),
                              ("setecentas", 700),
                              ("oitocentos", 800),
                              ("oitocentas", 800),
                              ("novecentos", 900),
                              ("novecentas", 900),
                              ("mil", 1000),
                              ("milhão", 1000000),
                              ("milhao", 1000000),
                              ("milhões", 1000000),
                              ("milhoes", 1000000),
                              ("bilhão", 1000000000),
                              ("bilhao", 1000000000),
                              ("bilhões", 1000000000),
                              ("bilhoes", 1000000000),
                              ("trilhão", 1000000000000),
                              ("trilhao", 1000000000000),
                              ("trilhões", 1000000000000),
                              ("trilhoes", 1000000000000)])
    OrdinalNumberMap = dict([("primeiro", 1),
                             ("primeira", 1),
                             ("segundo", 2),
                             ("segunda", 2),
                             ("terceiro", 3),
                             ("terceira", 3),
                             ("terço", 3),
                             ("terça", 3),
                             ("quarto", 4),
                             ("quarta", 4),
                             ("quinto", 5),
                             ("quinta", 5),
                             ("sexto", 6),
                             ("sexta", 6),
                             ("sétimo", 7),
                             ("setimo", 7),
                             ("sétima", 7),
                             ("setima", 7),
                             ("oitavo", 8),
                             ("oitava", 8),
                             ("nono", 9),
                             ("nona", 9),
                             ("décimo", 10),
                             ("decimo", 10),
                             ("décima", 10),
                             ("decima", 10),
                             ("undécimo", 11),
                             ("undecimo", 11),
                             ("undécima", 11),
                             ("undecima", 11),
                             ("duodécimo", 11),
                             ("duodecimo", 11),
                             ("duodécima", 11),
                             ("duodecima", 11),
                             ("vigésimo", 20),
                             ("vigesimo", 20),
                             ("vigésima", 20),
                             ("vigesima", 20),
                             ("trigésimo", 30),
                             ("trigesimo", 30),
                             ("trigésima", 30),
                             ("trigesima", 30),
                             ("quadragésimo", 40),
                             ("quadragesimo", 40),
                             ("quadragésima", 40),
                             ("quadragesima", 40),
                             ("quinquagésimo", 50),
                             ("quinquagesimo", 50),
                             ("quinquagésima", 50),
                             ("quinquagesima", 50),
                             ("sexagésimo", 60),
                             ("sexagesimo", 60),
                             ("sexagésima", 60),
                             ("sexagesima", 60),
                             ("septuagésimo", 70),
                             ("septuagesimo", 70),
                             ("septuagésima", 70),
                             ("septuagesima", 70),
                             ("setuagésimo", 70),
                             ("setuagesimo", 70),
                             ("setuagésima", 70),
                             ("setuagesima", 70),
                             ("octogésimo", 80),
                             ("octogesimo", 80),
                             ("octogésima", 80),
                             ("octogesima", 80),
                             ("nonagésimo", 90),
                             ("nonagesimo", 90),
                             ("nonagésima", 90),
                             ("nonagesima", 90),
                             ("centesimo", 100),
                             ("centésimo", 100),
                             ("centesima", 100),
                             ("centésima", 100),
                             ("ducentésimo", 200),
                             ("ducentesimo", 200),
                             ("ducentésima", 200),
                             ("ducentesima", 200),
                             ("tricentésimo", 300),
                             ("tricentesimo", 300),
                             ("tricentésima", 300),
                             ("tricentesima", 300),
                             ("trecentésimo", 300),
                             ("trecentesimo", 300),
                             ("trecentésima", 300),
                             ("trecentesima", 300),
                             ("quadringentésimo", 400),
                             ("quadringentesimo", 400),
                             ("quadringentésima", 400),
                             ("quadringentesima", 400),
                             ("quadrigentésimo", 400),
                             ("quadrigentesimo", 400),
                             ("quadrigentésima", 400),
                             ("quadrigentesima", 400),
                             ("quingentésimo", 500),
                             ("quingentesimo", 500),
                             ("quingentésima", 500),
                             ("quingentesima", 500),
                             ("sexcentésimo", 600),
                             ("sexcentesimo", 600),
                             ("sexcentésima", 600),
                             ("sexcentesima", 600),
                             ("seiscentésimo", 600),
                             ("seiscentesimo", 600),
                             ("seiscentésima", 600),
                             ("seiscentesima", 600),
                             ("septingentésimo", 700),
                             ("septingentesimo", 700),
                             ("septingentésima", 700),
                             ("septingentesima", 700),
                             ("setingentésimo", 700),
                             ("setingentesimo", 700),
                             ("setingentésima", 700),
                             ("setingentesima", 700),
                             ("octingentésimo", 800),
                             ("octingentesimo", 800),
                             ("octingentésima", 800),
                             ("octingentesima", 800),
                             ("noningentésimo", 900),
                             ("noningentesimo", 900),
                             ("noningentésima", 900),
                             ("noningentesima", 900),
                             ("nongentésimo", 900),
                             ("nongentesimo", 900),
                             ("nongentésima", 900),
                             ("nongentesima", 900),
                             ("milésimo", 1000),
                             ("milesimo", 1000),
                             ("milésima", 1000),
                             ("milesima", 1000),
                             ("milionésimo", 1000000),
                             ("milionesimo", 1000000),
                             ("milionésima", 1000000),
                             ("milionesima", 1000000),
                             ("bilionésimo", 1000000000),
                             ("bilionesimo", 1000000000),
                             ("bilionésima", 1000000000),
                             ("bilionesima", 1000000000)])
    PrefixCardinalMap = dict([("hum", 1),
                              ("um", 1),
                              ("dois", 2),
                              ("tres", 3),
                              ("três", 3),
                              ("quatro", 4),
                              ("cinco", 5),
                              ("seis", 6),
                              ("sete", 7),
                              ("oito", 8),
                              ("nove", 9),
                              ("dez", 10),
                              ("onze", 11),
                              ("doze", 12),
                              ("treze", 13),
                              ("catorze", 14),
                              ("quatorze", 14),
                              ("quinze", 15),
                              ("dezesseis", 16),
                              ("dezasseis", 16),
                              ("dezessete", 17),
                              ("dezassete", 17),
                              ("dezoito", 18),
                              ("dezenove", 19),
                              ("dezanove", 19),
                              ("vinte", 20),
                              ("trinta", 30),
                              ("quarenta", 40),
                              ("cinquenta", 50),
                              ("cincoenta", 50),
                              ("sessenta", 60),
                              ("setenta", 70),
                              ("oitenta", 80),
                              ("noventa", 90),
                              ("cem", 100),
                              ("duzentos", 200),
                              ("trezentos", 300),
                              ("quatrocentos", 400),
                              ("quinhentos", 500),
                              ("seiscentos", 600),
                              ("setecentos", 700),
                              ("oitocentos", 800),
                              ("novecentos", 900)])
    SuffixOrdinalMap = dict([("milesimo", 1000),
                             ("milionesimo", 1000000),
                             ("bilionesimo", 1000000000),
                             ("trilionesimo", 1000000000000)])
    RoundNumberMap = dict([("mil", 1000),
                           ("milesimo", 1000),
                           ("milhão", 1000000),
                           ("milhao", 1000000),
                           ("milhões", 1000000),
                           ("milhoes", 1000000),
                           ("milionésimo", 1000000),
                           ("milionesimo", 1000000),
                           ("bilhão", 1000000000),
                           ("bilhao", 1000000000),
                           ("bilhões", 1000000000),
                           ("bilhoes", 1000000000),
                           ("bilionésimo", 1000000000),
                           ("bilionesimo", 1000000000),
                           ("trilhão", 1000000000000),
                           ("trilhao", 1000000000000),
                           ("trilhões", 1000000000000),
                           ("trilhoes", 1000000000000),
                           ("trilionésimo", 1000000000000),
                           ("trilionesimo", 1000000000000),
                           ("dezena", 10),
                           ("dezenas", 10),
                           ("dúzia", 12),
                           ("duzia", 12),
                           ("dúzias", 12),
                           ("duzias", 12),
                           ("k", 1000),
                           ("m", 1000000),
                           ("g", 1000000000),
                           ("b", 1000000000),
                           ("t", 1000000000000)])
    AmbiguityFiltersDict = dict([("^[.]", "")])
    RelativeReferenceOffsetMap = dict([("proxima", "1"),
                                       ("proximo", "1"),
                                       ("próxima", "1"),
                                       ("próximo", "1"),
                                       ("proximas", "1"),
                                       ("proximos", "1"),
                                       ("próximas", "1"),
                                       ("próximos", "1"),
                                       ("ultima", "0"),
                                       ("ultimo", "0"),
                                       ("última", "0"),
                                       ("último", "0"),
                                       ("ultimas", "0"),
                                       ("ultimos", "0"),
                                       ("últimas", "0"),
                                       ("últimos", "0"),
                                       ("penultima", "-1"),
                                       ("penultimo", "-1"),
                                       ("penúltima", "-1"),
                                       ("penúltimo", "-1"),
                                       ("penultimas", "-1"),
                                       ("penultimos", "-1"),
                                       ("penúltimas", "-1"),
                                       ("penúltimos", "-1"),
                                       ("ultima mas um", "-1"),
                                       ("ultimo mas um", "-1"),
                                       ("última mas um", "-1"),
                                       ("último mas um", "-1"),
                                       ("anterior ao último", "-1"),
                                       ("anterior ao última", "-1"),
                                       ("antepenultima", "-2"),
                                       ("antepenultimo", "-2"),
                                       ("antepenúltima", "-2"),
                                       ("antepenúltimo", "-2"),
                                       ("antepenultimas", "-2"),
                                       ("antepenultimos", "-2"),
                                       ("antepenúltimas", "-2"),
                                       ("antepenúltimos", "-2"),
                                       ("seguinte", "1"),
                                       ("seguintes", "1"),
                                       ("anterior", "-1"),
                                       ("anteriores", "-1"),
                                       ("atual", "0"),
                                       ("atuais", "0")])
    RelativeReferenceRelativeToMap = dict([("proxima", "current"),
                                           ("proximo", "current"),
                                           ("próxima", "current"),
                                           ("próximo", "current"),
                                           ("proximas", "current"),
                                           ("proximos", "current"),
                                           ("próximas", "current"),
                                           ("próximos", "current"),
                                           ("ultima", "end"),
                                           ("ultimo", "end"),
                                           ("última", "end"),
                                           ("último", "end"),
                                           ("ultimas", "end"),
                                           ("ultimos", "end"),
                                           ("últimas", "end"),
                                           ("últimos", "end"),
                                           ("penultima", "end"),
                                           ("penultimo", "end"),
                                           ("penúltima", "end"),
                                           ("penúltimo", "end"),
                                           ("penultimas", "end"),
                                           ("penultimos", "end"),
                                           ("penúltimas", "end"),
                                           ("penúltimos", "end"),
                                           ("ultima mas um", "end"),
                                           ("ultimo mas um", "end"),
                                           ("última mas um", "end"),
                                           ("último mas um", "end"),
                                           ("anterior ao último", "end"),
                                           ("anterior ao última", "end"),
                                           ("antepenultima", "end"),
                                           ("antepenultimo", "end"),
                                           ("antepenúltima", "end"),
                                           ("antepenúltimo", "end"),
                                           ("antepenultimas", "end"),
                                           ("antepenultimos", "end"),
                                           ("antepenúltimas", "end"),
                                           ("antepenúltimos", "end"),
                                           ("seguinte", "current"),
                                           ("seguintes", "current"),
                                           ("anterior", "current"),
                                           ("anteriores", "current"),
                                           ("atual", "current"),
                                           ("atuais", "current")])
# pylint: enable=line-too-long