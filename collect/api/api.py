from urllib.parse import urlencode
from analysis_pd.collect.api.json_requests import json_request
import math
from datetime import datetime

def pd_gen_url(endpoint, service_key, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))
    return url


# 출입국 관광 통계 서비스
def pd_fetch_foreign_visitor(country_code='', year = 0, month = 0, service_key=''):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(endpoint,
                     service_key,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     NAT_CD = country_code,
                     ED_CD = 'E',
                     _type = 'json')
    json_result = json_request(url=url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')

    reslut_message = json_header.get('resultMsg')
    if 'OK' != reslut_message:
        print('%s Error[%s] for request %s' % (datetime.now(),reslut_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0, service_key=''):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    isnext = True
    pageNo = 1

    while isnext:
        url = pd_gen_url(endpoint,
                         service_key,
                         YM='{0:04d}{1:02d}'.format(year, month),
                         SIDO=district1,
                         GUNGU=district2,
                         RES_NM=tourspot,
                         numOfRows=100,
                         _type='json',
                         pageNo=pageNo)
        json_result = json_request(url=url)

        if json_result is None:
            break

        json_body = json_result.get('response').get('body')
        json_nor = None if json_result is None else json_body.get('numOfRows')
        json_tc = None if json_result is None else json_body.get('totalCount')

        json_items = json_body.get('items')

        json_lp = math.ceil(json_tc/json_nor)

        if pageNo == json_lp:
            isnext = False
        else:
            pageNo += 1

        yield json_items.get('item')