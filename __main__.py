import collect
from config import CONFIG

if __name__ == '__main__':

    # colletion
    collect.crawlling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    for country in CONFIG['countries']:
        collect.crawlling_foreign_visitor(country, **CONFIG['common'])


    # analysis

    # visualize