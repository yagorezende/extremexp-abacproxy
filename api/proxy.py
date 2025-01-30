import requests
from flask import request, jsonify
from flask.views import View


class Proxy(View):
    init_every_request = False

    def dispatch_request(self):
        # print("Here!")
        # get the target URL from the 'to' query parameter
        target_url = request.args.get('to')
        # print("target_url", target_url)

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
