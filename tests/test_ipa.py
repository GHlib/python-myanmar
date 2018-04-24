#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from myanmar.romanizer import romanize, IPA


def test_ipa_romanizer():
    # fixme..IPA of "ငါးဥ" is ŋəʔṵ
    assert romanize("ငါးဥ", IPA) == "ŋáʔṵ"
    assert romanize("ကတ်ဝက်", IPA) == "kaʔwɛʔ"
    assert romanize("အက်ယန်", IPA) == "ʔɛʔjàɴ"
    assert romanize("ဆီပုံး", IPA) == "sʰìbóʊɴ"
    assert romanize("ပါကေး", IPA) == "pàgé"
    assert romanize("ဂေါက်", IPA) == "ɡaʊʔ"
    assert romanize("မြန်မာ", IPA) == "mjàɴmà"
    # fixme..IPA of "စာရေး" is səjé
    assert romanize("စာရေး", IPA) == "sàjé"
    assert romanize("စာအုပ်", IPA) == "sàʔoʊʔ"
    assert romanize("စာရွက်စာတမ်း", IPA) == "sàjwɛʔsàdáɴ"
    # fixme..IPA of "သူငယ်" is θəŋɛ̀
    assert romanize("သူငယ်", IPA) == "θùŋɛ̀"
    assert romanize("ကွန်ပျူတာ", IPA) == "kʊ̀ɴpjùtà"
    # fixme..IPA of "ဝက်ဝံ" is wɛʔwʊ̀ɴ
    assert romanize("ဝက်ဝံ", IPA) == "wɛʔwàɴ"
    # fixme..IPA of "ဆရာဝန်" is sʰa̰jàwʊ̀ɴ
    assert romanize("ဆရာဝန်", IPA) == "sʰəjàwàɴ"
    assert romanize("မျက်စိ", IPA) == "mjɛʔsḭ"
    assert romanize("တန်ဂါ", IPA) == "tàɴɡà"
    assert romanize("ဒူးထောက်", IPA) == "dútʰaʊʔ"
    assert romanize("တာငါ", IPA) == "tàŋà"
    assert romanize("ခလုတ်", IPA) == "kʰəloʊʔ"
    assert romanize("ဆန်ပြုတ်", IPA) == "sʰàɴbjoʊʔ"
    assert romanize("လျှင်", IPA) == "l̥jɪ̀ɴ"
    assert romanize("ဘဲ", IPA) == "bɛ́"
    # fixme..IPA of "ဓာတ်" is daʔ
    assert romanize("ဓာတ်", IPA) == "dæt"
    assert romanize("ယား", IPA) == "já"
    assert romanize("ခုန်", IPA) == "kʰòʊɴ"
    assert romanize("နမ်း", IPA) == "náɴ"
    assert romanize("နှမ်း", IPA) == "n̥áɴ"
    assert romanize("ခံ", IPA) == "kʰàɴ"
    # fix..IPA of "ညစ်" is ɲiʔ
    assert romanize("ညစ်", IPA) == "ɲɪʔ"
    assert romanize("ဟစ်", IPA) == "hɪʔ"
    assert romanize("ငါး", IPA) == "ŋá"
    assert romanize("ပဲ", IPA) == "pɛ́"
    assert romanize("ဖဲ", IPA) == "pʰɛ́"
    # fixme..IPA of "တိရစ္ဆာန်" is təɹeiʔsʰàɴ
    assert romanize("တိရစ္ဆာန်", IPA) == "tḭjɪʔsʰààɴ"
    # fixme..IPA of "အညာသား" is ʔəɲàðá
    assert romanize("အညာသား", IPA) == "ʔəɲàθá"
    assert romanize("စာ", IPA) == "sà"
    assert romanize("ဆာ", IPA) == "sʰà"
    assert romanize("ရှာ", IPA) == "ʃà"
    assert romanize("တတ်", IPA) == "taʔ"
    assert romanize("ထပ်", IPA) == "tʰaʔ"
    assert romanize("သတ်", IPA) == "θaʔ"
    assert romanize("ဝါး", IPA) == "wá"
    assert romanize("ဝှက်", IPA) == "w̥ɛʔ"
    assert romanize("ဇာ", IPA) == "zà"
    assert romanize("နား", IPA) == "ná"
    # fixme..IPA of "နိုင်" is nàɪ̯ɴ
    assert romanize("နိုင်", IPA) == "nàɪɴ"
    # fixme..IPA of "နောက်" is naʊ̯ʔ
    assert romanize("နောက်", IPA) == "naʊʔ"
    assert romanize("ပေါက်", IPA) == "paʊʔ"
    assert romanize("အောက်", IPA) == "ʔaʊʔ"
    assert romanize("နေ", IPA) == "nè"
    assert romanize("နိပ်", IPA) == "neɪʔ"
    assert romanize("နယ်", IPA) == "nɛ̀"
    assert romanize("နီး", IPA) == "ní"
    assert romanize("နင်း", IPA) == "nɪ́ɴ"
    assert romanize("နို့", IPA) == "no̰"
    # fixme..IPA of "နုန်း" is nóʊ̯ɴ
    assert romanize("နုန်း", IPA) == "nóʊɴ"
    assert romanize("နော်", IPA) == "nɔ̀"
    assert romanize("နှူး", IPA) == "n̥ú"
    assert romanize("နွမ်း", IPA) == "nʊ́ɴ"
    assert romanize("ငါ", IPA) == "ŋà"
    assert romanize("ငါး", IPA) == "ŋá"
    assert romanize("ဓါး", IPA) == "dá"
    assert romanize("ငါ့", IPA) == "ŋa̰"
    assert romanize("ဂင်းနီဗစ်ဆော", IPA) == "ɡɪ́ɴnìbɪʔsʰɔ́"
    assert romanize("ဂဏန်းတွက်စက်", IPA) == "ɡənáɴtwɛʔsɛʔ"
    assert romanize("စွံ", IPA) == "swàɴ"
    assert romanize("ဂွ", IPA) == "ɡw"
    assert romanize("ငံပြာရည်", IPA) == "ŋàɴpjàjì"
    # fixme..IPA of "စက်ဘီး" is sɛʔbéɪɴ
    assert romanize("စက်ဘီး", IPA) == "sɛʔbí"
    assert romanize("စက်ဆုပ်", IPA) == "sɛʔsʰoʊʔ"
    assert romanize("ပြုံယမ်း", IPA) == "pjòʊɴjáɴ"
    assert romanize("ဖုန်စုပ်စက်", IPA) == "pʰòʊɴsoʊʔsɛʔ"
    assert romanize("ဖာလူဒါ", IPA) == "pʰàlùdà"
    assert romanize("ဖူး", IPA) == "pʰú"
    assert romanize("ပျား", IPA) == "pjá"
    assert romanize("ဖွား", IPA) == "pʰwá"
    assert romanize("ရက်ကန်း", IPA) == "jɛʔkáɴ"
    assert romanize("ရှင်ရှင်", IPA) == "ʃɪ̀ɴʃɪ̀ɴ"
    # fixme..IPA of "လက်ကိုင်ပဝါ" is lɛʔkàɪɴpa̰wà
    assert romanize("လက်ကိုင်ပဝါ", IPA) == "lɛʔkàɪɴpəwà"
    assert romanize("လက်ကောက်", IPA) == "lɛʔkaʊʔ"
    assert romanize("လက်နက်", IPA) == "lɛʔnɛʔ"
    assert romanize("လက်မှတ်", IPA) == "lɛʔm̥aʔ"
    assert romanize("လတ်ဗီယာ", IPA) == "laʔbìjà"
    assert romanize("လိပ်စာ", IPA) == "leɪʔsà"
    assert romanize("ရွေးကောက်ပွဲ", IPA) == "jwékaʊʔpwɛ́"
    assert romanize("လူငယ်", IPA) == "lùŋɛ̀"
    assert romanize("ချင်", IPA) == "tɕʰɪ̀ɴ"
    assert romanize("ကြဉ်", IPA) == "tɕɪ̀ɴ"
    assert romanize("စီးပွားရေး", IPA) == "síbwájé"
    assert romanize("စတေဒီယံ", IPA) == "sətèdìjàɴ"