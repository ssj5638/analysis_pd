from urllib.parse import urlencode
from analysis_pd.collect.api.json_requests import json_request


BASE_URL_PD_API = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
ACCESS_TOKEN = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'


def pd_gen_url(endpoint=BASE_URL_PD_API, **params):

    url = '%s?%s' % (endpoint, urlencode(params))
    return url


def pd_fetch_tourspot_visitor(district1 = '', district2 = '', tourspot = '', year = 0, month = 0):
    url = pd_gen_url(ym = year sido = district1, gungu=district2, res_nm=tourspot,
                     serviceKey=ACCESS_TOKEN)
    json_result = json_request(url = url)

    print(json_result)