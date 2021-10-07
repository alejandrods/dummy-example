# -*- coding: utf-8 -*-

import json
import flask
import logging
from flask import json
from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

# Logs
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(message)s')


@app.route('/predict', methods=['POST'])
@cross_origin()
def prediction():
    """
    Function to receive an user query and return response

    :return: Dummy response
    """

    income_query = json.loads(flask.request.data)['instances']

    logging.info('Query received: {}'.format(income_query))

    res = {
            "predictions": [
                {
                    "body": {'query': income_query}
                }
            ],
        }

    response = app.response_class(response=json.dumps(res),
                                  status=200,
                                  mimetype='application/json')
    return response


@app.route('/health')
@cross_origin()
def health_check():
    """
    Check status code

    :return:
    """

    response = app.response_class(response=json.dumps({'status': 'success'}),
                                  status=200,
                                  mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)

