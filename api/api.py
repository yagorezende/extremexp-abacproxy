import logging

import requests
from flask import request, jsonify
from flask.views import View
from flask_restx import Namespace, Resource, reqparse

api: Namespace = Namespace('Proxy', description='ExtremeXP Proxy')

parser = reqparse.RequestParser()
parser.add_argument('to', type=str, required=True, help='URL to proxy to')

@api.route("/", methods=['GET', 'POST', 'HEAD', 'OPTIONS', 'DELETE', 'PUT', 'TRACE', 'PATCH'])
class Proxy(View):
    init_every_request = False

    def __init__(self, _api=None, *args, **kwargs):
        self.api = _api

    def dispatch_request(self):
        # get the target URL from the 'to' query parameter
        target_url = request.args.get('to')
        if not target_url:
            return jsonify({"error": "Missing 'to' parameter"}), 400

        # Forward the request to the target URL
        try:
            response = requests.request(
                method=request.method,
                url=target_url,
                headers={key: value for key, value in request.headers if key != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )

            # forward response to the caller
            return response.content, response.status_code, response.headers.items()
        except Exception as e:
            return jsonify({"error": str(e)}), 500