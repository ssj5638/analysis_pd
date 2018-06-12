from analysis_pd.collect.api import api

# test for pd_gen_url
url = api.pd_gen_url('http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
                     YM = '{0:04d}{1:02d}'.format(2017, 1),
                     SIDO= '부산광역시',
                     GUNGU = '해운대구',
                     RES_NM = '부산시립미술관',
                     numOfRows = 10,
                     _type='json',
                     pageNo=1)
print(url)

# test for pd_fetch_tourspot_visitor
api.pd_fetch_tourspot_visitor(district1 = '부산광역시', year = 2012, month = 7)