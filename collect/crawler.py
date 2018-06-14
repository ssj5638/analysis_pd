from .api import api
import json
import os


RESULT_DIRECTORY = '__results__/crawlling'


def preprocess(data):
    # 국내 관광객
    if 'csNatCnt' not in data:
        data['count_locals'] = 0
    else:
        data['count_locals'] = data['csNatCnt']

    # 국외 관광객
    if 'csForCnt' not in data:
        data['count_forigner'] = 0
    else:
        data['count_forigner'] = data['csForCnt']

    # 관광지
    if 'resNm' not in data:
        data['tourist_spot'] = 0
    else:
        data['tourist_spot'] = data['resNm']

    # date
    if 'ym' not in data:
        data['date'] = 0
    else:
        data['date'] = data['ym']

    # 시, 도
    if 'sido' not in data:
        data['restrict1'] = 0
    else:
        data['restrict1'] = data['sido']

    # 구, 군
    if 'gungu' not in data:
        data['restrict2'] = 0
    else:
        data['restrict2'] = data['gungu']


def crawlling_tourspot_visitor(district, start_year, end_year):
    result = []
    filename = '%s/%s_touristspot_%s_%s.json'.format(RESULT_DIRECTORY, district, start_year, end_year)

    for year in range(start_year, end_year+1):
        for month in range(1, 13, 1):
            for items in api.pd_fetch_tourspot_visitor(district, year=year, month=month):
                for data in items:
                    preprocess(data)
                    result += data


    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(result,
                   indent = 4,
                   sort_keys = True,
                   ensure_ascii = False)  # 아스키 코드로만 구성되어있는가?
        outfile.write(json_string)

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)