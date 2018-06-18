from .api import api
import json


# tourspot 전처리
def preprocess_tourspot_visitor(data):
    del data['addrCd']
    del data['rnum']

    # 국내 관광객
    if 'csNatCnt' not in data:
        data['count_locals'] = 0
    else:
        data['count_locals'] = data['csNatCnt']
        del data['csNatCnt']

    # 국외 관광객
    if 'csForCnt' not in data:
        data['count_forigner'] = 0
    else:
        data['count_forigner'] = data['csForCnt']
        del data['csForCnt']

    # 관광지
    if 'resNm' not in data:
        data['tourist_spot'] = 0
    else:
        data['tourist_spot'] = data['resNm']
        del data['resNm']

    # date
    if 'ym' not in data:
        data['date'] = 0
    else:
        data['date'] = data['ym']
        del data['ym']

    # 시, 도
    if 'sido' not in data:
        data['restrict1'] = 0
    else:
        data['restrict1'] = data['sido']
        del data['sido']

    # 구, 군
    if 'gungu' not in data:
        data['restrict2'] = 0
    else:
        data['restrict2'] = data['gungu']
        del data['gungu']


# foreign 전처리
def preprocess_foreign_visitor(data):
    del data['ed']
    del data['edCd']
    del data['rnum']

    # 나라 코드
    data['country_code'] = data['natCd']
    del data['natCd']

    # 나라 이름
    data['country_name'] = data['natKorNm'].replace(' ','')
    del data['natKorNm']

    # 방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년월
    if 'ym' not in data:
        data['date'] = 0
    else:
        data['date'] = data['ym']
        del data['ym']


# tourspot 크롤링
def crawlling_tourspot_visitor(district, start_year, end_year, fetch=True, result_directory='', service_key=''):
    results = []
    filename = '%s/%s_touristspot_%s_%s.json' % (result_directory, district, start_year, end_year)
    if fetch:
        for year    in range(start_year, end_year+1):
            for month in range(1, 13, 1):
                for items in api.pd_fetch_tourspot_visitor(district, year=year, month=month, service_key=service_key):
                    for data in items:
                        preprocess_tourspot_visitor(data)
                        results.append(data)

        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent = 4, sort_keys = False, ensure_ascii = False)
            outfile.write(json_string)


# foreign 크롤링
def crawlling_foreign_visitor(country, start_year, end_year, fetch=True, result_directory='', service_key=''):
    results= []

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range (1, 13):
                data = api.pd_fetch_foreign_visitor(country[1], year, month, service_key)
                if data is None:
                    continue        # 반복문의 처음으로 돌아가기

                preprocess_foreign_visitor(data)
                results.append(data)

        # save data to file
        filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (result_directory, country[0], country[1], start_year, end_year)

        with open(filename, 'w', encoding='utf-8') as outfile:      # 쓰기 모드 'w'
            json_string = json.dumps(results,
                                         indent=4,
                                         sort_keys=True,
                                         ensure_ascii=False)            # indent는 들여쓰기 // ensure_ascii는 아스키 코드로만 구성되어있는가?
            outfile.write(json_string)


