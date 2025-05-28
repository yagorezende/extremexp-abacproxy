import requests
from flask import request, jsonify
from flask.views import View


class Proxy(View):
    init_every_request = False
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'TRACE', 'CONNECT']

    def dispatch_request(self):
        # print("Here!")
        # get the target URL from the 'to' query parameter
        target_url = request.args.get('to')
        # print("target_url", target_url)

        if not target_url:
            return jsonify({"error": "Missing 'to' parameter"}), 400

        # Forward the request to the target URL
        try:
            content = dict(
                method=request.method,
                url=target_url,
                headers={key: value for key, value in request.headers if key != 'Host'},
                cookies=request.cookies,
                allow_redirects=False,
            )

            if request.method in {'POST', 'PUT', 'PATCH'}:
                content['data'] = request.get_data()
            elif request.method == 'GET':
                query_params = request.args.to_dict()
                # remove 'to' from query parameters to avoid infinite loop
                query_params.pop('to', None)
                content['params'] = query_params

            response = requests.request(**content)

            # check if the response is chunked
            if response.headers.get('Transfer-Encoding') == 'chunked':
                del response.headers['Transfer-Encoding']
            # forward response to the caller
            return response.content, response.status_code, response.headers.items()
        except Exception as e:
            return jsonify({"error": str(e)}), 500
