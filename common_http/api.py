from collections import OrderedDict

import simplejson
from flask import current_app, make_response
from flask_restplus import Api


def ourinvest_output_json(data, code, headers=None):
    settings = current_app.config.get("RESTPLUS_JSON", {})
    if current_app.debug:
        settings.setdefault("indent", 4)
    dumped = simplejson.dumps(data, **settings) + "\n"
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


class OurinvestAPI(Api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.representations = OrderedDict(
            [("application/json", ourinvest_output_json)])
