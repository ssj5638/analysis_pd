from analysis_pd.collect.api import api
import json

# test for pd_gen_url
url = api.pd_gen_url('http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
                     YM = '{0:04d}{1:02d}'.format(2012, 7),
                     SIDO= '서울특별시',
                     GUNGU = '',
                     RES_NM = '',
                     numOfRows = 10,
                     _type ='json',
                     pageNo = 1)
print(url)

# test for pd_tourspot_visitor
#for item in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
#    print(item)

for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    print(items)



