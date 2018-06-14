from analysis_pd.collect.api import api


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
for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2017, month=7):
    print(items)

# test for pd_fetch_foreign_visitor
item = api.pd_fetch_foreign_visitor(112, 2017, 7)
print(item)

