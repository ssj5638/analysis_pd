from urllib.parse import urlencode
from analysis_pd.collect.api.json_requests import json_request
from urllib.parse import quote_plus


BASE_URL_PD_API = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
ACCESS_TOKEN = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'


def pd_gen_url(endpoint=BASE_URL_PD_API, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, ACCESS_TOKEN, urlencode(params))
    return url


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    url = pd_gen_url(YM='{0:04d}{1:02d}'.format(year, month),
                     SIDO = district1,
                     GUNGU = district2,
                     RES_NM = tourspot,
                     numOfRows=10,
                     _type = 'json')

    while True:
        json_result = json_request(url=url)
        json_1 = json_result.get('response')
        json_2 = json_1.get('body')

        page = json_2.get('pageNo')
        totalcnt = json_2.get('totalCount')

        json_3 = json_2.get('items')

        if page == totalcnt:
            break

        return json_3.get('item')

