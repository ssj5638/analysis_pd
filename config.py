import os


CONFIG = {
    'district' : '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {'start_year': 2017,
               'end_year': 2017,
               'fetch': True,
               'result_directory':'__results__/crawlling',
               'service_key':'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'
               }

}

# 해당 디렉토리가 없으면 새로 만들기
if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])