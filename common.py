YIELD_STEPS = ['3개월', '6개월', '1년', '2년', '3년', '5년', '10년']
YIELD_GAP_INFO = ['Yield Gap (10 yr - 3mo)', 'GDP wighted Yield Gap']
GDP = ['GDP', 'GDP Ratio']

COUNTRIES = [
    "캐나다",
    "미국",
    "오스트리아",
    "벨기에",
    "덴마크",
    "핀란드",
    "독일",
    "아일랜드",
    "이스라엘",
    "이태리",
    "네덜란드",
    "노르웨이",
    "포르투갈",
    "스페인",
    "스웨덴",
    "스위스",
    "영국",
    "호주",
    "중국",
    "홍콩",
    "일본",
    "뉴질랜드",
    "싱가폴",
    "한국",
    "베트남"
]

HISTORY_TARGET = [
    '미국', '중국', '한국', '일본', '영국', '독일'
]

COLUMNS = ['국가'] + GDP + YIELD_STEPS + YIELD_GAP_INFO
ROWS = ['국가'] + COUNTRIES
