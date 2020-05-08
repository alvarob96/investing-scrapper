# Copyright 2018-2020 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.


FINANCIAL_SUMMARY_TYPES = {
    'income_statement': 0,
    'balance_sheet': 1,
    'cash_flow_statement': 2
}

FINANCIAL_SUMMARY_PERIODS = {
    "annual": "Annual",
    "quarterly": "Interim"
}

PRODUCT_FILTERS = {
    'indices': 'indice', 
    'stocks': 'equities', 
    'etfs': 'etf', 
    'funds': 'fund', 
    'commodities': 'commodity', 
    'currencies': 'currency', 
    'cryptos': 'crypto', 
    'bonds': 'bond', 
    'certificates': 'certificate', 
    'fxfutures': 'fxfuture'
}

PAIR_FILTERS = {
    'indice': 'indices', 
    'equities': 'stocks', 
    'etf': 'etfs', 
    'fund': 'funds', 
    'commodity': 'commodities', 
    'currency': 'currencies', 
    'crypto': 'cryptos', 
    'bond': 'bonds', 
    'certificate': 'certificates', 
    'fxfuture': 'fxfutures'
}

FLAG_FILTERS = {
    'Andorra': 'andorra', 'Argentina': 'argentina', 'Australia': 'australia', 'Austria': 'austria',
    'Bahrain': 'bahrain', 'Bangladesh': 'bangladesh', 'Belgium': 'belgium', 'Bermuda': 'bermuda', 
    'Bosnia': 'bosnia', 'Botswana': 'botswana', 'Brazil': 'brazil', 'Bulgaria': 'bulgaria', 
    'Canada': 'canada', 'Cayman_Islands': 'cayman islands', 'Chile': 'chile', 'China': 'china', 
    'Colombia': 'colombia', 'Costa_Rica': 'costa rica', 'Cote_dIvoire': 'ivory coast', 
    'Croatia': 'croatia', 'Cyprus': 'cyprus', 'Czech_Republic': 'czech republic', 
    'Denmark': 'denmark', 'Ecuador': 'ecuador', 'Egypt': 'egypt', 'Estonia': 'estonia', 
    'Europe': 'euro zone', 'Finland': 'finland', 'France': 'france', 'Germany': 'germany', 
    'Gibraltar': 'gibraltar', 'Greece': 'greece', 'Hong_Kong': 'hong kong', 'Hungary': 'hungary', 
    'Iceland': 'iceland', 'India': 'india', 'Indonesia': 'indonesia', 'Iraq': 'iraq', 
    'Ireland': 'ireland', 'Israel': 'israel', 'Italy': 'italy', 'Jamaica': 'jamaica', 
    'Japan': 'japan', 'Jordan': 'jordan', 'Kazakhstan': 'kazakhstan', 'Kenya': 'kenya', 
    'Kuwait': 'kuwait', 'Latvia': 'latvia', 'Lebanon': 'lebanon', 'Liechtenstein': 'liechtenstein', 
    'Lithuania': 'lithuania', 'Luxembourg': 'luxembourg', 'Malawi': 'malawi', 'Malaysia': 'malaysia', 
    'Malta': 'malta', 'Mauritius': 'mauritius', 'Mexico': 'mexico', 'Monaco': 'monaco', 
    'Mongolia': 'mongolia', 'Montenegro': 'montenegro', 'Morocco': 'morocco', 'Namibia': 'namibia', 
    'Netherlands': 'netherlands', 'New_Zealand': 'new zealand', 'Nigeria': 'nigeria', 
    'Norway': 'norway', 'Oman': 'oman', 'Pakistan': 'pakistan', 'Palestine': 'palestine', 
    'Peru': 'peru', 'Philippines': 'philippines', 'Poland': 'poland', 'Portugal': 'portugal', 
    'Qatar': 'qatar', 'Romania': 'romania', 'Russian_Federation': 'russia', 'Rwanda': 'rwanda', 
    'Saudi_Arabia': 'saudi arabia', 'Serbia': 'serbia', 'Singapore': 'singapore', 'Slovakia': 'slovakia', 
    'Slovenia': 'slovenia', 'South_Africa': 'south africa', 'South_Korea': 'south korea', 
    'Spain': 'spain', 'Sri_Lanka': 'sri lanka', 'Sweden': 'sweden', 'Switzerland': 'switzerland', 
    'Taiwan': 'taiwan', 'Tanzania': 'tanzania', 'Thailand': 'thailand', 'Tunisia': 'tunisia', 
    'Turkey': 'turkey', 'Uganda': 'uganda', 'Ukraine': 'ukraine', 'Dubai': 'dubai', 
    'UK': 'united kingdom', 'USA': 'united states', 'Venezuela': 'venezuela', 'Vietnam': 'vietnam', 
    'Zambia': 'zambia', 'Zimbabwe': 'zimbabwe'
}

COUNTRY_FILTERS = {
    'andorra': 'Andorra', 'argentina': 'Argentina', 'australia': 'Australia', 'austria': 'Austria', 
    'bahrain': 'Bahrain', 'bangladesh': 'Bangladesh', 'belgium': 'Belgium', 'bermuda': 'Bermuda', 
    'bosnia': 'Bosnia', 'botswana': 'Botswana', 'brazil': 'Brazil', 'bulgaria': 'Bulgaria', 
    'canada': 'Canada', 'cayman islands': 'Cayman_Islands', 'chile': 'Chile', 'china': 'China', 
    'colombia': 'Colombia', 'costa rica': 'Costa_Rica', 'ivory coast': 'Cote_dIvoire', 'croatia': 'Croatia', 
    'cyprus': 'Cyprus', 'czech republic': 'Czech_Republic', 'denmark': 'Denmark', 'ecuador': 'Ecuador', 
    'egypt': 'Egypt', 'estonia': 'Estonia', 'euro zone': 'Europe', 'finland': 'Finland', 'france': 'France', 
    'germany': 'Germany', 'gibraltar': 'Gibraltar', 'greece': 'Greece', 'hong kong': 'Hong_Kong', 
    'hungary': 'Hungary', 'iceland': 'Iceland', 'india': 'India', 'indonesia': 'Indonesia', 
    'iraq': 'Iraq', 'ireland': 'Ireland', 'israel': 'Israel', 'italy': 'Italy', 'jamaica': 'Jamaica', 
    'japan': 'Japan', 'jordan': 'Jordan', 'kazakhstan': 'Kazakhstan', 'kenya': 'Kenya', 'kuwait': 'Kuwait', 
    'latvia': 'Latvia', 'lebanon': 'Lebanon', 'liechtenstein': 'Liechtenstein', 'lithuania': 'Lithuania', 
    'luxembourg': 'Luxembourg', 'malawi': 'Malawi', 'south korea': 'South_Korea', 'spain': 'Spain', 
    'sri lanka': 'Sri_Lanka', 'sweden': 'Sweden', 'switzerland': 'Switzerland', 'taiwan': 'Taiwan', 
    'tanzania': 'Tanzania', 'thailand': 'Thailand', 'tunisia': 'Tunisia', 'turkey': 'Turkey', 'uganda': 'Uganda', 
    'ukraine': 'Ukraine', 'dubai': 'Dubai', 'united kingdom': 'UK', 'united states': 'USA', 'venezuela': 'Venezuela', 
    'vietnam': 'Vietnam', 'zambia': 'Zambia', 'zimbabwe': 'Zimbabwe', 'mauritius': 'Mauritius', 'mexico': 'Mexico', 
    'monaco': 'Monaco', 'mongolia': 'Mongolia', 'montenegro': 'Montenegro', 'morocco': 'Morocco', 'namibia': 'Namibia', 
    'netherlands': 'Netherlands', 'new zealand': 'New_Zealand', 'nigeria': 'Nigeria', 'norway': 'Norway', 'oman': 'Oman', 
    'pakistan': 'Pakistan', 'palestine': 'Palestine', 'peru': 'Peru', 'philippines': 'Philippines', 'poland': 'Poland', 
    'portugal': 'Portugal', 'qatar': 'Qatar', 'romania': 'Romania', 'russia': 'Russian_Federation', 'rwanda': 'Rwanda', 
    'saudi arabia': 'Saudi_Arabia', 'serbia': 'Serbia', 'singapore': 'Singapore', 'slovakia': 'Slovakia', 'slovenia': 'Slovenia', 
    'south africa': 'South_Africa', 'south korea': 'South_Korea', 'spain': 'Spain', 'sri lanka': 'Sri_Lanka', 'sweden': 'Sweden', 
    'switzerland': 'Switzerland', 'taiwan': 'Taiwan', 'tanzania': 'Tanzania', 'thailand': 'Thailand', 'tunisia': 'Tunisia', 
    'turkey': 'Turkey', 'uganda': 'Uganda', 'ukraine': 'Ukraine', 'dubai': 'Dubai', 'united kingdom': 'UK', 'united states': 'USA', 
    'venezuela': 'Venezuela', 'vietnam': 'Vietnam', 'zambia': 'Zambia', 'zimbabwe': 'Zimbabwe'
}

CATEGORY_FILTERS = {
    'credit': '_credit',
    'employment': '_employment',
    'economic_activity': '_economicActivity',
    'inflation': '_inflation',
    'central_banks': '_centralBanks',
    'confidence': '_confidenceIndex',
    'balance': '_balance',
    'bonds': '_Bonds'
}

IMPORTANCE_RATINGS = {
    1: 'low',
    2: 'medium',
    3: 'high'
}

COUNTRY_ID_FILTERS = {
    'argentina': 29, 'australia': 25, 'austria': 54, 'bahrain': 145, 'bangladesh': 47, 'belgium': 34, 'bosnia': 174,
    'botswana': 163, 'brazil': 32, 'bulgaria': 70, 'canada': 6, 'cayman islands': 232, 'chile': 27, 'china': 37, 'colombia': 122,
    'costa rica': 15, 'croatia': 113, 'cyprus': 107, 'czech republic': 55, 'denmark': 24, 'dubai': 143, 'ecuador': 121, 'egypt': 59,
    'estonia': 89, 'euro zone': 72, 'finland': 71, 'france': 22, 'germany': 17, 'greece': 51, 'hong kong': 39, 'hungary': 93, 
    'iceland': 106, 'india': 14, 'indonesia': 48, 'iraq': 66, 'ireland': 33, 'israel': 23, 'italy': 10, 'ivory coast': 78, 'jamaica': 119, 
    'japan': 35, 'jordan': 92, 'kazakhstan': 102, 'kenya': 57, 'kuwait': 94, 'latvia': 97, 'lebanon': 68, 'lithuania': 96, 'luxembourg': 103, 
    'malawi': 111, 'malaysia': 42, 'malta': 109, 'mauritius': 188, 'mexico': 7, 'mongolia': 139, 'montenegro': 247, 'morocco': 105, 
    'namibia': 172, 'netherlands': 21, 'new zealand': 43, 'nigeria': 20, 'norway': 60, 'oman': 87, 'pakistan': 44, 'palestine': 193, 
    'peru': 125, 'philippines': 45, 'poland': 53, 'portugal': 38, 'qatar': 170, 'romania': 100, 'russia': 56, 'rwanda': 80, 'saudi arabia': 52, 
    'serbia': 238, 'singapore': 36, 'slovakia': 90, 'slovenia': 112, 'south africa': 110, 'south korea': 11, 'spain': 26, 'sri lanka': 162,  
    'sweden': 9, 'switzerland': 12, 'taiwan': 46, 'tanzania': 85, 'thailand': 41, 'tunisia': 202, 'turkey': 63, 'uganda': 123, 'ukraine': 61, 
    'united kingdom': 4, 'united states': 5, 'venezuela': 138, 'vietnam': 178, 'zambia': 84, 'zimbabwe': 75
}

TIME_FILTERS = {
    'time_remaining': 'timeRemain',
    'time_only': 'timeOnly'
}

TIMEZONES = {
    'GMT -11:00': [2, 35], 'GMT -10:00': [3], 'GMT -9:00': [4], 'GMT -8:00': [36, 5], 'GMT -7:00': [37, 38, 6], 
    'GMT -6:00': [39, 7, 40, 41], 'GMT -5:00': [42, 8, 43], 'GMT -4:00': [10, 9, 45, 46], 
    'GMT -3:30': [11], 'GMT -3:00': [44, 12, 48, 49, 50, 51, 47], 'GMT -1:00': [14, 53], 'GMT': [55, 15, 56],
    'GMT +1:00': [16, 57, 58, 54, 166, 59, 60], 'GMT +2:00': [62, 64, 65, 66, 68, 17, 67, 61], 'GMT +3:00': [71, 63, 70, 18, 72], 
    'GMT +3:30': [19], 'GMT +4:00': [20, 73], 'GMT +4:30': [21], 'GMT +5:00': [22, 77], 'GMT +5:30': [23, 79], 'GMT +5:45': [24], 
    'GMT +6:00': [25], 'GMT +6:30': [26], 'GMT +7:00': [27], 'GMT +8:00': [178, 28, 113], 'GMT +9:00': [29, 88], 'GMT +9:30': [90], 
    'GMT +10:30': [30], 'GMT +11:00': [31, 32], 'GMT +12:00': [1], 'GMT +13:00': [33]
}

PRODUCT_TYPE_FILES = {
    'certificate': 'certificates.csv',
    'commodity': 'commodities.csv',
    'currency_cross': 'currency_crosses.csv',
    'etf': 'etfs.csv',
    'fund': 'funds.csv',
    'index': 'indices.csv',
    'stock': 'stocks.csv',
    'bond': 'bonds.csv'
}

INTERVAL_FILTERS = {
    '5mins': 60*5,
    '15mins': 60*15,
    '30mins': 60*30,
    '1hour': 60*60,
    '5hours': 60*60*5,
    'daily': 60*60*24,
    'weekly': 'week',
    'monthly': 'month'
}

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",
    "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8",
    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",
    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5",
    "Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2",
    "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre",
    "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre",
    "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2",
    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2",
    "Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14",
    "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
]

BOND_COUNTRIES = [
    {'exchange_id': 37, 'tag': 'argentina', 'country_id': 29, 'country': 'argentina'}, {'exchange_id': 18, 'tag': 'australia', 'country_id': 25, 'country': 'australia'},
    {'exchange_id': 17, 'tag': 'austria', 'country_id': 54, 'country': 'austria'}, {'exchange_id': 39, 'tag': 'bahrain', 'country_id': 145, 'country': 'bahrain'},
    {'exchange_id': 115, 'tag': 'bangladesh', 'country_id': 47, 'country': 'bangladesh'}, {'exchange_id': 14, 'tag': 'belgium', 'country_id': 34, 'country': 'belgium'},
    {'exchange_id': 77, 'tag': 'botswana', 'country_id': 163, 'country': 'botswana'}, {'exchange_id': 47, 'tag': 'brazil', 'country_id': 32, 'country': 'brazil'},
    {'exchange_id': 44, 'tag': 'bulgaria', 'country_id': 70, 'country': 'bulgaria'}, {'exchange_id': 51, 'tag': 'canada', 'country_id': 6, 'country': 'canada'},
    {'exchange_id': 42, 'tag': 'chile', 'country_id': 27, 'country': 'chile'}, {'exchange_id': 54, 'tag': 'china', 'country_id': 37, 'country': 'china'},
    {'exchange_id': 55, 'tag': 'colombia', 'country_id': 122, 'country': 'colombia'}, {'exchange_id': 45, 'tag': 'croatia', 'country_id': 113, 'country': 'croatia'},
    {'exchange_id': 78, 'tag': 'cyprus', 'country_id': 107, 'country': 'cyprus'}, {'exchange_id': 56, 'tag': 'czech-republic', 'country_id': 55, 'country': 'czech republic'},
    {'exchange_id': 15, 'tag': 'denmark', 'country_id': 24, 'country': 'denmark'}, {'exchange_id': 33, 'tag': 'egypt', 'country_id': 59, 'country': 'egypt'},
    {'exchange_id': 16, 'tag': 'finland', 'country_id': 71, 'country': 'finland'}, {'exchange_id': 9, 'tag': 'france', 'country_id': 22, 'country': 'france'},
    {'exchange_id': 4, 'tag': 'germany', 'country_id': 17, 'country': 'germany'}, {'exchange_id': 41, 'tag': 'greece', 'country_id': 51, 'country': 'greece'},
    {'exchange_id': 21, 'tag': 'hong-kong', 'country_id': 39, 'country': 'hong kong'}, {'exchange_id': 23, 'tag': 'hungary', 'country_id': 93, 'country': 'hungary'},
    {'exchange_id': 52, 'tag': 'iceland', 'country_id': 106, 'country': 'iceland'}, {'exchange_id': 46, 'tag': 'india', 'country_id': 14, 'country': 'india'},
    {'exchange_id': 57, 'tag': 'indonesia', 'country_id': 48, 'country': 'indonesia'}, {'exchange_id': 58, 'tag': 'ireland', 'country_id': 33, 'country': 'ireland'},
    {'exchange_id': 26, 'tag': 'israel', 'country_id': 23, 'country': 'israel'}, {'exchange_id': 6, 'tag': 'italy', 'country_id': 10, 'country': 'italy'},
    {'exchange_id': 20, 'tag': 'japan', 'country_id': 35, 'country': 'japan'}, {'exchange_id': 29, 'tag': 'jordan', 'country_id': 92, 'country': 'jordan'},
    {'exchange_id': 59, 'tag': 'kenya', 'country_id': 57, 'country': 'kenya'}, {'exchange_id': 80, 'tag': 'latvia', 'country_id': 97, 'country': 'latvia'},
    {'exchange_id': 81, 'tag': 'lithuania', 'country_id': 96, 'country': 'lithuania'}, {'exchange_id': 61, 'tag': 'luxembourg', 'country_id': 103, 'country': 'luxembourg'},
    {'exchange_id': 62, 'tag': 'malaysia', 'country_id': 42, 'country': 'malaysia'}, {'exchange_id': 82, 'tag': 'malta', 'country_id': 109, 'country': 'malta'},
    {'exchange_id': 86, 'tag': 'mauritius', 'country_id': 188, 'country': 'mauritius'}, {'exchange_id': 53, 'tag': 'mexico', 'country_id': 7, 'country': 'mexico'},
    {'exchange_id': 36, 'tag': 'morocco', 'country_id': 105, 'country': 'morocco'}, {'exchange_id': 75, 'tag': 'namibia', 'country_id': 172, 'country': 'namibia'},
    {'exchange_id': 7, 'tag': 'netherlands', 'country_id': 21, 'country': 'netherlands'}, {'exchange_id': 83, 'tag': 'new-zealand', 'country_id': 43, 'country': 'new zealand'},
    {'exchange_id': 96, 'tag': 'nigeria', 'country_id': 20, 'country': 'nigeria'}, {'exchange_id': 8, 'tag': 'norway', 'country_id': 60, 'country': 'norway'},
    {'exchange_id': 63, 'tag': 'pakistan', 'country_id': 44, 'country': 'pakistan'}, {'exchange_id': 64, 'tag': 'peru', 'country_id': 125, 'country': 'peru'},
    {'exchange_id': 65, 'tag': 'philippines', 'country_id': 45, 'country': 'philippines'}, {'exchange_id': 25, 'tag': 'poland', 'country_id': 53, 'country': 'poland'},
    {'exchange_id': 10, 'tag': 'portugal', 'country_id': 38, 'country': 'portugal'}, {'exchange_id': 35, 'tag': 'qatar', 'country_id': 170, 'country': 'qatar'},
    {'exchange_id': 43, 'tag': 'romania', 'country_id': 100, 'country': 'romania'}, {'exchange_id': 40, 'tag': 'russia', 'country_id': 56, 'country': 'russia'},
    {'exchange_id': 28, 'tag': 'saudi-arabia', 'country_id': 52, 'country': 'saudi arabia'}, {'exchange_id': 102, 'tag': 'serbia', 'country_id': 238, 'country': 'serbia'},
    {'exchange_id': 19, 'tag': 'singapore', 'country_id': 36, 'country': 'singapore'}, {'exchange_id': 84, 'tag': 'slovakia', 'country_id': 90, 'country': 'slovakia'},
    {'exchange_id': 66, 'tag': 'slovenia', 'country_id': 112, 'country': 'slovenia'}, {'exchange_id': 22, 'tag': 'south-africa', 'country_id': 110, 'country': 'south africa'},
    {'exchange_id': 60, 'tag': 'south-korea', 'country_id': 11, 'country': 'south korea'}, {'exchange_id': 11, 'tag': 'spain', 'country_id': 26, 'country': 'spain'},
    {'exchange_id': 67, 'tag': 'sri-lanka', 'country_id': 162, 'country': 'sri lanka'}, {'exchange_id': 12, 'tag': 'sweden', 'country_id': 9, 'country': 'sweden'},
    {'exchange_id': 5, 'tag': 'switzerland', 'country_id': 12, 'country': 'switzerland'}, {'exchange_id': 68, 'tag': 'taiwan', 'country_id': 46, 'country': 'taiwan'},
    {'exchange_id': 69, 'tag': 'thailand', 'country_id': 41, 'country': 'thailand'}, {'exchange_id': 49, 'tag': 'turkey', 'country_id': 63, 'country': 'turkey'},
    {'exchange_id': 76, 'tag': 'uganda', 'country_id': 123, 'country': 'uganda'}, {'exchange_id': 70, 'tag': 'ukraine', 'country_id': 61, 'country': 'ukraine'},
    {'exchange_id': 3, 'tag': 'uk', 'country_id': 4, 'country': 'united kingdom'}, {'exchange_id': 1, 'tag': 'usa', 'country_id': 5, 'country': 'united states'},
    {'exchange_id': 71, 'tag': 'venezuela', 'country_id': 138, 'country': 'venezuela'}, {'exchange_id': 72, 'tag': 'vietnam', 'country_id': 178, 'country': 'vietnam'}
]

CERTIFICATE_COUNTRIES = [
    {'country': 'france', 'id': 22}, {'country': 'germany', 'id': 17},
    {'country': 'italy', 'id': 10}, {'country': 'netherlands', 'id': 21},
    {'country': 'sweden', 'id': 9}
]

CURRENCIES = [
    {'symbol': 'AED', 'name': 'UAE Dirham', 'value': 22}, {'symbol': 'AFN', 'name': 'Afghanistan Afghani', 'value': 93}, {'symbol': 'ALL', 'name': 'Albanian Lek', 'value': 58},
    {'symbol': 'AMD', 'name': 'Armenian Dram', 'value': 158}, {'symbol': 'ANG', 'name': 'Antilles Guilder', 'value': 95}, {'symbol': 'AOA', 'name': 'Angolan kwanza', 'value': 159},
    {'symbol': 'ARS', 'name': 'Argentinian Peso', 'value': 32}, {'symbol': 'AUD', 'name': 'Australian Dollar', 'value': 1}, {'symbol': 'AZN', 'name': 'Azerbaijani Manat', 'value': 161},
    {'symbol': 'BAM', 'name': 'Bosnia Herzegovina Mark', 'value': 96}, {'symbol': 'BBD', 'name': 'Barbadian Dollar', 'value': 33}, {'symbol': 'BDT', 'name': 'Bangladeshi Taka', 'value': 59},
    {'symbol': 'BGN', 'name': 'Bulgarian Lev', 'value': 91}, {'symbol': 'BHD', 'name': 'Baharain Dinar', 'value': 36}, {'symbol': 'BIF', 'name': 'Burundian Franc', 'value': 98},
    {'symbol': 'BND', 'name': 'Brunei Dollar', 'value': 37}, {'symbol': 'BOB', 'name': 'Bolivian Boliviano', 'value': 99}, {'symbol': 'BRL', 'name': 'Brazil Real', 'value': 35},
    {'symbol': 'BRLT', 'name': 'Brazilian Real Tourism', 'value': 1896}, {'symbol': 'BSD', 'name': 'Bahamas Dollar', 'value': 38}, {'symbol': 'BWP', 'name': 'Botswana Pula', 'value': 39},
    {'symbol': 'BYN', 'name': 'Belarusian Ruble', 'value': 100}, {'symbol': 'BZD', 'name': 'Belize Dollar', 'value': 101}, {'symbol': 'CAD', 'name': 'Canadian Dollar', 'value': 15},
    {'symbol': 'CHF', 'name': 'Swiss Franc', 'value': 4}, {'symbol': 'CLP', 'name': 'Chilean Peso', 'value': 40}, {'symbol': 'CNH', 'name': 'Chinese Yuan Offshore', 'value': 194},
    {'symbol': 'CNY', 'name': 'Chinese Yuan', 'value': 41}, {'symbol': 'COP', 'name': 'Colombian Peso', 'value': 92}, {'symbol': 'CRC', 'name': 'Costa Rican Colon', 'value': 42},
    {'symbol': 'CUP', 'name': 'Cuban Peso', 'value': 102}, {'symbol': 'CVE', 'name': 'Cape Verdean Escudo', 'value': 188}, {'symbol': 'CZK', 'name': 'Czech Koruna', 'value': 16},
    {'symbol': 'DJF', 'name': 'Djiboutian Franc', 'value': 44}, {'symbol': 'DKK', 'name': 'Danish Krone', 'value': 6}, {'symbol': 'DOP', 'name': 'Dominican Peso', 'value': 45},
    {'symbol': 'DZD', 'name': 'Algerian Dinar', 'value': 104}, {'symbol': 'EGP', 'name': 'Egyptian Pound', 'value': 47}, {'symbol': 'ETB', 'name': 'Ethiopian Birr', 'value': 48},
    {'symbol': 'EUR', 'name': 'Euro', 'value': 17}, {'symbol': 'FJD', 'name': 'Fiji Dollar', 'value': 49}, {'symbol': 'GBP', 'name': 'British Pound', 'value': 3},
    {'symbol': 'GEL', 'name': 'Georgian lari', 'value': 183}, {'symbol': 'GHS', 'name': 'Ghanaian Cedi', 'value': 50}, {'symbol': 'GMD', 'name': 'Gambian Dalasi', 'value': 51},
    {'symbol': 'GNF', 'name': 'Guinean Franc', 'value': 107}, {'symbol': 'GTQ', 'name': 'Guatemalan Quetzal', 'value': 52}, {'symbol': 'HKD', 'name': 'Hong Kong Dollar', 'value': 20},
    {'symbol': 'HNL', 'name': 'Honduran Lempira', 'value': 53}, {'symbol': 'HRK', 'name': 'Croatian Kuna', 'value': 109}, {'symbol': 'HTG', 'name': 'Haitian Gourde', 'value': 54},
    {'symbol': 'HUF', 'name': 'Hungarian Forint', 'value': 11}, {'symbol': 'IDR', 'name': 'Indonesian Rupiah', 'value': 55}, {'symbol': 'ILS', 'name': 'Israeli Shekel', 'value': 23},
    {'symbol': 'INR', 'name': 'Indian Rupee', 'value': 29}, {'symbol': 'IQD', 'name': 'Iraqi Dinar', 'value': 56}, {'symbol': 'IRR', 'name': 'Iranian Rial', 'value': 57},
    {'symbol': 'ISK', 'name': 'Icelandic Kr', 'value': 60}, {'symbol': 'JMD', 'name': 'Jamaican Dollar', 'value': 61}, {'symbol': 'JOD', 'name': 'Jordan Dinar', 'value': 24},
    {'symbol': 'JPY', 'name': 'Japanese Yen', 'value': 2}, {'symbol': 'KES', 'name': 'Kenyan Shilling', 'value': 110}, {'symbol': 'KGS', 'name': 'Kyrgyzstan som', 'value': 168},
    {'symbol': 'KHR', 'name': 'Cambodian Riel', 'value': 111}, {'symbol': 'KMF', 'name': 'Comorian Franc', 'value': 169}, {'symbol': 'KRW', 'name': 'Korean Won', 'value': 28},
    {'symbol': 'KWD', 'name': 'Kuwaiti Dinar', 'value': 25}, {'symbol': 'KYD', 'name': 'Cayman Islands Dollar', 'value': 62}, {'symbol': 'KZT', 'name': 'Kazakh Tenge', 'value': 63},
    {'symbol': 'LAK', 'name': 'Lao Kip', 'value': 113}, {'symbol': 'LBP', 'name': 'Lebanese Pound', 'value': 114}, {'symbol': 'LKR', 'name': 'Sri Lankan Rupee', 'value': 115},
    {'symbol': 'LSL', 'name': 'Lesotho loti', 'value': 185}, {'symbol': 'LYD', 'name': 'Libyan Dinar', 'value': 119}, {'symbol': 'MAD', 'name': 'Moroccan Dirham', 'value': 64},
    {'symbol': 'MDL', 'name': 'Moldovan Leu', 'value': 181}, {'symbol': 'MGA', 'name': 'Malagasy Ariary', 'value': 121}, {'symbol': 'MKD', 'name': 'Macedonian Denar', 'value': 123},
    {'symbol': 'MMK', 'name': 'Myanmar kyat', 'value': 124}, {'symbol': 'MNT', 'name': 'Mongolian Tugrik', 'value': 196}, {'symbol': 'MOP', 'name': 'Macanese Pataca', 'value': 125},
    {'symbol': 'MRU', 'name': 'Mauritanian ouguiya', 'value': 126}, {'symbol': 'MUR', 'name': 'Mauritian Rupee', 'value': 66}, {'symbol': 'MVR', 'name': 'Maldivian Rufiyaa', 'value': 170},
    {'symbol': 'MWK', 'name': 'Malawian Kwacha', 'value': 67}, {'symbol': 'MXN', 'name': 'Mexican Peso', 'value': 14}, {'symbol': 'MYR', 'name': 'Malaysian Ringgit', 'value': 68},
    {'symbol': 'MZN', 'name': 'Mozambican Metical', 'value': 192}, {'symbol': 'NAD', 'name': 'Namibian Dollar', 'value': 128}, {'symbol': 'NGN', 'name': 'Nigerian Naira', 'value': 69},
    {'symbol': 'NIO', 'name': 'Nicaraguan Córdoba', 'value': 70}, {'symbol': 'NOK', 'name': 'Norwegian Krone', 'value': 7}, {'symbol': 'NPR', 'name': 'Nepalese Rupee', 'value': 129},
    {'symbol': 'NZD', 'name': 'New Zealand Dollar', 'value': 5}, {'symbol': 'OMR', 'name': 'Omani Rial', 'value': 71}, {'symbol': 'PAB', 'name': 'Panamanian Balboa', 'value': 130},
    {'symbol': 'PEN', 'name': 'Peru Sol', 'value': 72}, {'symbol': 'PGK', 'name': 'Papua New Guinean Kina', 'value': 73}, {'symbol': 'PHP', 'name': 'Philippine Peso', 'value': 74},
    {'symbol': 'PKR', 'name': 'Pakistani Rupee', 'value': 75}, {'symbol': 'PLN', 'name': 'Polish Zloty', 'value': 8}, {'symbol': 'PYG', 'name': 'Paraguayan Guarani', 'value': 131},
    {'symbol': 'QAR', 'name': 'Qatari Riyal', 'value': 76}, {'symbol': 'RON', 'name': 'Romanian Leu', 'value': 78}, {'symbol': 'RSD', 'name': 'Serbian Dinar', 'value': 133},
    {'symbol': 'RUB', 'name': 'Russian Ruble', 'value': 79}, {'symbol': 'RWF', 'name': 'Rwandan Franc', 'value': 134}, {'symbol': 'SAR', 'name': 'Saudi Riyal', 'value': 26},
    {'symbol': 'SCR', 'name': 'Seychelles Rupee', 'value': 81}, {'symbol': 'SDG', 'name': 'Sudanese Pound', 'value': 136}, {'symbol': 'SEK', 'name': 'Swedish Krona', 'value': 18},
    {'symbol': 'SGD', 'name': 'Singapore Dollar', 'value': 19}, {'symbol': 'SOS', 'name': 'Somali Shilling', 'value': 139}, {'symbol': 'STN', 'name': 'São Tomé/Príncipe Dobra', 'value': 141},
    {'symbol': 'SVC', 'name': 'El Salvador Colon', 'value': 142}, {'symbol': 'SYP', 'name': 'Syrian Pound', 'value': 143}, {'symbol': 'SZL', 'name': 'Swazi Lilangeni', 'value': 82},
    {'symbol': 'THB', 'name': 'Thai Baht', 'value': 10}, {'symbol': 'TJS', 'name': 'Tajikistani somoni', 'value': 193}, {'symbol': 'TMT', 'name': 'Turkmenistan manat', 'value': 1746},
    {'symbol': 'TND', 'name': 'Tunisian Dinar', 'value': 83}, {'symbol': 'TRY', 'name': 'Turkish Lira', 'value': 9}, {'symbol': 'TTD', 'name': 'Trinidad Dollar', 'value': 84},
    {'symbol': 'TWD', 'name': 'Taiwan Dollar', 'value': 34}, {'symbol': 'TZS', 'name': 'Tanzanian Shilling', 'value': 145}, {'symbol': 'UAH', 'name': 'Ukrainian Hryvnia', 'value': 85},
    {'symbol': 'UGX', 'name': 'Ugandan Shilling', 'value': 146}, {'symbol': 'USD', 'name': 'US Dollar', 'value': 12}, {'symbol': 'UYU', 'name': 'Uruguayan Peso', 'value': 147},
    {'symbol': 'UZS', 'name': 'Uzbekistani Sum', 'value': 148}, {'symbol': 'VES', 'name': 'Venezuelan Bolivar', 'value': 149}, {'symbol': 'VND', 'name': 'Vietnamese Dong', 'value': 87},
    {'symbol': 'VUV', 'name': 'Vanuatu vatu', 'value': 177}, {'symbol': 'XAF', 'name': 'Central African Franc', 'value': 150}, {'symbol': 'XAGg', 'name': 'Gram Silver', 'value': 216},
    {'symbol': 'XBR', 'name': 'Brent Spot', 'value': 1683}, {'symbol': 'XCD', 'name': 'East Caribbean Dollar', 'value': 179}, {'symbol': 'XOF', 'name': 'West African CFA franc', 'value': 151},
    {'symbol': 'XPF', 'name': 'French Pacific Franc', 'value': 88}, {'symbol': 'YER', 'name': 'Yemeni Rial', 'value': 153}, {'symbol': 'ZAR', 'name': 'South African Rand', 'value': 13},
    {'symbol': 'ZMW', 'name': 'Zambia Kwacha', 'value': 155}
]

ETF_COUNTRIES = [
    {'country': 'australia', 'code': 'au'}, {'country': 'austria', 'code': 'at'}, {'country': 'belgium', 'code': 'be'}, {'country': 'brazil', 'code': 'br'}, {'country': 'bulgaria', 'code': 'bg'},
    {'country': 'canada', 'code': 'ca'}, {'country': 'china', 'code': 'cn'}, {'country': 'colombia', 'code': 'co'}, {'country': 'denmark', 'code': 'dk'}, {'country': 'egypt', 'code': 'eg'},
    {'country': 'euro zone', 'code': 'eu'}, {'country': 'finland', 'code': 'fi'}, {'country': 'france', 'code': 'fr'}, {'country': 'germany', 'code': 'de'}, {'country': 'greece', 'code': 'gr'},
    {'country': 'hong kong', 'code': 'hk'}, {'country': 'hungary', 'code': 'hu'}, {'country': 'iceland', 'code': 'is'}, {'country': 'india', 'code': 'in'}, {'country': 'indonesia', 'code': 'id'},
    {'country': 'ireland', 'code': 'ie'}, {'country': 'israel', 'code': 'il'}, {'country': 'italy', 'code': 'it'}, {'country': 'japan', 'code': 'jp'}, {'country': 'malaysia', 'code': 'my'},
    {'country': 'mexico', 'code': 'mx'}, {'country': 'netherlands', 'code': 'nl'}, {'country': 'new zealand', 'code': 'nz'}, {'country': 'nigeria', 'code': 'ng'}, {'country': 'norway', 'code': 'no'},
    {'country': 'peru', 'code': 'pe'}, {'country': 'poland', 'code': 'pl'}, {'country': 'portugal', 'code': 'pt'}, {'country': 'qatar', 'code': 'qa'}, {'country': 'romania', 'code': 'ro'},
    {'country': 'russia', 'code': 'ru'}, {'country': 'saudi arabia', 'code': 'sa'}, {'country': 'singapore', 'code': 'sg'}, {'country': 'south africa', 'code': 'sa'}, {'country': 'south korea', 'code': 'kr'},
    {'country': 'spain', 'code': 'es'}, {'country': 'sweden', 'code': 'se'}, {'country': 'switzerland', 'code': 'ch'}, {'country': 'taiwan', 'code': 'tw'}, {'country': 'thailand', 'code': 'th'},
    {'country': 'turkey', 'code': 'tr'}, {'country': 'uk', 'code': 'uk'}, {'country': 'usa', 'code': 'us'}, {'country': 'vietnam', 'code': 'vn'}
]

FUND_COUNTRIES = [
    {'country': 'andorra', 'id': 206}, {'country': 'australia', 'id': 25}, {'country': 'austria', 'id': 54}, {'country': 'bahrain', 'id': 145}, {'country': 'belgium', 'id': 34},
    {'country': 'bermuda', 'id': 8}, {'country': 'brazil', 'id': 32}, {'country': 'canada', 'id': 6}, {'country': 'cayman islands', 'id': 232}, {'country': 'chile', 'id': 27},
    {'country': 'china', 'id': 37}, {'country': 'czech republic', 'id': 55}, {'country': 'denmark', 'id': 24}, {'country': 'estonia', 'id': 89}, {'country': 'finland', 'id': 71},
    {'country': 'france', 'id': 22}, {'country': 'germany', 'id': 17}, {'country': 'gibraltar', 'id': 147}, {'country': 'greece', 'id': 51}, {'country': 'hong kong', 'id': 39},
    {'country': 'hungary', 'id': 93}, {'country': 'iceland', 'id': 106}, {'country': 'india', 'id': 14}, {'country': 'indonesia', 'id': 48}, {'country': 'ireland', 'id': 33},
    {'country': 'israel', 'id': 23}, {'country': 'italy', 'id': 10}, {'country': 'japan', 'id': 35}, {'country': 'latvia', 'id': 97}, {'country': 'liechtenstein', 'id': 190},
    {'country': 'lithuania', 'id': 96}, {'country': 'luxembourg', 'id': 103}, {'country': 'malaysia', 'id': 42}, {'country': 'malta', 'id': 109}, {'country': 'mauritius', 'id': 188},
    {'country': 'mexico', 'id': 7}, {'country': 'monaco', 'id': 115}, {'country': 'namibia', 'id': 172}, {'country': 'netherlands', 'id': 21}, {'country': 'new zealand', 'id': 43},
    {'country': 'norway', 'id': 60}, {'country': 'oman', 'id': 87}, {'country': 'pakistan', 'id': 44}, {'country': 'philippines', 'id': 45}, {'country': 'poland', 'id': 53},
    {'country': 'portugal', 'id': 38}, {'country': 'qatar', 'id': 170}, {'country': 'russia', 'id': 56}, {'country': 'saudi arabia', 'id': 52}, {'country': 'singapore', 'id': 36},
    {'country': 'slovenia', 'id': 112}, {'country': 'south africa', 'id': 110}, {'country': 'south korea', 'id': 11}, {'country': 'spain', 'id': 26}, {'country': 'sweden', 'id': 9},
    {'country': 'switzerland', 'id': 12}, {'country': 'taiwan', 'id': 46}, {'country': 'thailand', 'id': 41}, {'country': 'united arab emirates', 'id': 143}, {'country': 'uk', 'id': 4},
    {'country': 'usa', 'id': 5}, {'country': 'vietnam', 'id': 178}
]

STOCK_COUNTRIES = [
    {'country': 'argentina', 'id': 10141}, {'country': 'brazil', 'id': 602}, {'country': 'canada', 'id': 608}, {'country': 'chile', 'id': 10150}, {'country': 'colombia', 'id': 723},
    {'country': 'costa rica', 'id': 688}, {'country': 'jamaica', 'id': 10210}, {'country': 'mexico', 'id': 612}, {'country': 'peru', 'id': 722}, {'country': 'united states', 'id': 800},
    {'country': 'venezuela', 'id': 25920001}, {'country': 'austria', 'id': 10124}, {'country': 'belgium', 'id': 10121}, {'country': 'bosnia', 'id': 804}, {'country': 'bulgaria', 'id': 10151},
    {'country': 'croatia', 'id': 10148}, {'country': 'cyprus', 'id': 725}, {'country': 'czech republic', 'id': 614}, {'country': 'denmark', 'id': 10122}, {'country': 'finland', 'id': 10123},
    {'country': 'france', 'id': 10112}, {'country': 'germany', 'id': 10106}, {'country': 'greece', 'id': 10145}, {'country': 'hungary', 'id': 10128}, {'country': 'iceland', 'id': 610},
    {'country': 'ireland', 'id': 616}, {'country': 'italy', 'id': 10109}, {'country': 'luxembourg', 'id': 802}, {'country': 'malta', 'id': 803}, {'country': 'montenegro', 'id': 10213},
    {'country': 'netherlands', 'id': 10110}, {'country': 'norway', 'id': 10111}, {'country': 'poland', 'id': 10130}, {'country': 'portugal', 'id': 10113}, {'country': 'romania', 'id': 10149},
    {'country': 'russia', 'id': 10144}, {'country': 'serbia', 'id': 805}, {'country': 'slovakia', 'id': 625}, {'country': 'slovenia', 'id': 620}, {'country': 'spain', 'id': 10119},
    {'country': 'sweden', 'id': 10120}, {'country': 'switzerland', 'id': 10107}, {'country': 'turkey', 'id': 606}, {'country': 'ukraine', 'id': 623}, {'country': 'united kingdom', 'id': 801},
    {'country': 'australia', 'id': 10125}, {'country': 'bangladesh', 'id': 10201}, {'country': 'china', 'id': 724}, {'country': 'hong kong', 'id': 10126}, {'country': 'india', 'id': 600},
    {'country': 'indonesia', 'id': 615}, {'country': 'japan', 'id': 692}, {'country': 'kazakhstan', 'id': 10207}, {'country': 'malaysia', 'id': 618}, {'country': 'mongolia', 'id': 10216},
    {'country': 'new zealand', 'id': 27525828}, {'country': 'pakistan', 'id': 619}, {'country': 'philippines', 'id': 721}, {'country': 'singapore', 'id': 10129}, {'country': 'south korea', 'id': 694},
    {'country': 'sri lanka', 'id': 621}, {'country': 'taiwan', 'id': 622}, {'country': 'thailand', 'id': 720}, {'country': 'vietnam', 'id': 624}, {'country': 'bahrain', 'id': 10143},
    {'country': 'egypt', 'id': 10136}, {'country': 'iraq', 'id': 10204}, {'country': 'israel', 'id': 10131}, {'country': 'jordan', 'id': 10134}, {'country': 'kuwait', 'id': 10132},
    {'country': 'lebanon', 'id': 10146}, {'country': 'oman', 'id': 10142}, {'country': 'palestine', 'id': 10137}, {'country': 'qatar', 'id': 10139}, {'country': 'saudi arabia', 'id': 10133},
    {'country': 'dubai', 'id': 10135}, {'country': 'botswana', 'id': 656}, {'country': 'ivory coast', 'id': 729}, {'country': 'kenya', 'id': 617}, {'country': 'malawi', 'id': 680},
    {'country': 'mauritius', 'id': 678}, {'country': 'morocco', 'id': 10147}, {'country': 'namibia', 'id': 652}, {'country': 'nigeria', 'id': 628}, {'country': 'rwanda', 'id': 686},
    {'country': 'south africa', 'id': 10127}, {'country': 'tanzania', 'id': 682}, {'country': 'tunisia', 'id': 604}, {'country': 'uganda', 'id': 654}, {'country': 'zambia', 'id': 25957877},
    {'country': 'zimbabwe', 'id': 684}
]

INDEX_COUNTRIES = [
    {'country': 'argentina', 'country_name': 'argentina'}, {'country': 'australia', 'country_name': 'australia'}, {'country': 'austria', 'country_name': 'austria'},
    {'country': 'bahrain', 'country_name': 'bahrain'}, {'country': 'bangladesh', 'country_name': 'bangladesh'}, {'country': 'belgium', 'country_name': 'belgium'},
    {'country': 'bosnia', 'country_name': 'bosnia-herzegovina'}, {'country': 'botswana', 'country_name': 'botswana'}, {'country': 'brazil', 'country_name': 'brazil'},
    {'country': 'bulgaria', 'country_name': 'bulgaria'}, {'country': 'canada', 'country_name': 'canada'}, {'country': 'chile', 'country_name': 'chile'},
    {'country': 'china', 'country_name': 'china'}, {'country': 'colombia', 'country_name': 'colombia'}, {'country': 'costa rica', 'country_name': 'costa rica'}, 
    {'country': 'ivory coast', 'country_name': "cote d'ivoire"}, {'country': 'croatia', 'country_name': 'croatia'}, {'country': 'cyprus', 'country_name': 'cyprus'}, 
    {'country': 'czech republic', 'country_name': 'czech republic'}, {'country': 'denmark', 'country_name': 'denmark'}, {'country': 'ecuador', 'country_name': 'ecuador'},
    {'country': 'egypt', 'country_name': 'egypt'}, {'country': 'estonia', 'country_name': 'estonia'}, {'country': 'finland', 'country_name': 'finland'}, 
    {'country': 'france', 'country_name': 'france'}, {'country': 'germany', 'country_name': 'germany'}, {'country': 'greece', 'country_name': 'greece'},
    {'country': 'hong kong', 'country_name': 'hong kong'}, {'country': 'hungary', 'country_name': 'hungary'}, {'country': 'iceland', 'country_name': 'iceland'},
    {'country': 'india', 'country_name': 'india'}, {'country': 'indonesia', 'country_name': 'indonesia'}, {'country': 'iraq', 'country_name': 'iraq'}, 
    {'country': 'ireland', 'country_name': 'ireland'}, {'country': 'israeli', 'country_name': 'israel'}, {'country': 'italy', 'country_name': 'italy'}, 
    {'country': 'jamaica', 'country_name': 'jamaica'}, {'country': 'japan', 'country_name': 'japan'}, {'country': 'jordan', 'country_name': 'jordan'},
    {'country': 'kazakhstan', 'country_name': 'kazakhstan'}, {'country': 'kenya', 'country_name': 'kenya'}, {'country': 'kuwaiti', 'country_name': 'kuwait'},
    {'country': 'latvia', 'country_name': 'latvia'}, {'country': 'lebanon', 'country_name': 'lebanon'}, {'country': 'lithuania', 'country_name': 'lithuania'}, 
    {'country': 'luxembourg', 'country_name': 'luxembourg'}, {'country': 'malawi', 'country_name': 'malawi'}, {'country': 'malaysia', 'country_name': 'malaysia'},
    {'country': 'malta', 'country_name': 'malta'}, {'country': 'mauritius', 'country_name': 'mauritius'}, {'country': 'mexico', 'country_name': 'mexico'}, 
    {'country': 'mongolia', 'country_name': 'mongolia'}, {'country': 'montenegro', 'country_name': 'montenegro'}, {'country': 'morocco', 'country_name': 'morocco'},
    {'country': 'namibia', 'country_name': 'namibia'}, {'country': 'netherlands', 'country_name': 'netherlands'}, {'country': 'new zealand', 'country_name': 'new zealand'},
    {'country': 'nigeria', 'country_name': 'nigeria'}, {'country': 'norway', 'country_name': 'norway'}, {'country': 'oman', 'country_name': 'oman'},
    {'country': 'pakistan', 'country_name': 'pakistan'}, {'country': 'palestine', 'country_name': 'palestinian territory'}, {'country': 'peru', 'country_name': 'peru'},
    {'country': 'philippines', 'country_name': 'philippines'}, {'country': 'poland', 'country_name': 'poland'}, {'country': 'portugal', 'country_name': 'portugal'},
    {'country': 'qatar', 'country_name': 'qatar'}, {'country': 'romania', 'country_name': 'romania'}, {'country': 'russia', 'country_name': 'russia'}, 
    {'country': 'rwanda', 'country_name': 'rwanda'}, {'country': 'saudi arabia', 'country_name': 'saudi arabia'}, {'country': 'serbia', 'country_name': 'serbia'},
    {'country': 'singapore', 'country_name': 'singapore'}, {'country': 'slovakia', 'country_name': 'slovakia'},{'country': 'slovenia', 'country_name': 'slovenia'}, 
    {'country': 'south africa', 'country_name': 'south africa'}, {'country': 'south korea', 'country_name': 'south korea'}, {'country': 'spain', 'country_name': 'spain'},
    {'country': 'sri lanka', 'country_name': 'sri lanka'}, {'country': 'sweden', 'country_name': 'sweden'}, {'country': 'switzerland', 'country_name': 'switzerland'},
    {'country': 'taiwan', 'country_name': 'taiwan'}, {'country': 'tanzania', 'country_name': 'tanzania'}, {'country': 'thailand', 'country_name': 'thailand'},
    {'country': 'tunisia', 'country_name': 'tunisia'}, {'country': 'turkey', 'country_name': 'turkey'}, {'country': 'uganda', 'country_name': 'uganda'},
    {'country': 'ukraine', 'country_name': 'ukraine'}, {'country': 'dubai', 'country_name': 'united arab emirates'}, {'country': 'uk', 'country_name': 'united kingdom'},
    {'country': 'usa', 'country_name': 'united states'}, {'country': 'venezuela', 'country_name': 'venezuela'}, {'country': 'vietnam', 'country_name': 'vietnam'},
    {'country': 'zambia', 'country_name': 'zambia'}, {'country': 'zimbabwe', 'country_name': 'zimbabwe'}
]
