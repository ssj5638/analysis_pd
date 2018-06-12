from urllib.request import Request, urlopen
import json
import sys
from datetime import *

def json_request(url = '', encoding = 'utf-8', success = None,
                 error = lambda e : print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        json_body = resp.read().decode(encoding)

        json_result = json.loads(json_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)
    except Exception as e:
        if callable(error) is True:
            error(e)