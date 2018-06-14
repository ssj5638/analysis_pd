from urllib.parse import urlencode
from analysis_pd.collect.api.json_requests import json_request
import math


BASE_URL_PD_API = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
ACCESS_TOKEN = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'


def pd_gen_url(endpoint=BASE_URL_PD_API, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, ACCESS_TOKEN, urlencode(params))
    return url


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):

    isnext = True
    pageNo = 1

    while isnext:
        url = pd_gen_url(YM='{0:04d}{1:02d}'.format(year, month),
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