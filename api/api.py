import logging

import requests
from flask import request
from flask_restx import Namespace, Resource, reqparse

api: Namespace = Namespace('Proxy', description='ExtremeXP Proxy')

parser = reqparse.RequestParser()
parser.add_argument('to', type=str, required=True, help='URL to proxy to')

@api.route("/", methods=['GET'])
class Proxy(Resource):
    @api.doc('proxy')
    def get(self):
        """
        Proxy request
        """
        args = parser.parse_args()
        to = args.get('to')
        headers = request.headers

        response = requests.get(to)
        self.api.app.logger.warning(f"Proxying request to {to}")
        self.api.app.logger.warning(response.content)
        return response.json(), response.status_code