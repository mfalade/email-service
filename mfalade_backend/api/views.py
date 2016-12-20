"""Views to handle all api requests."""
import json

from flask import jsonify, make_response, request
from flask_cors import CORS

from mfalade_backend import dispatcher
from mfalade_backend.api import api


CORS(api)


@api.route('/healthcheck')
def healthcheck():
    """Return app status."""
    return make_response(jsonify({
        'status_code': 200,
        'text': 'OK'
    }))


@api.route('/sendmail', methods=['POST'])
def sendmail():
    dispatcher.send_email(request.json)
    return json.dumps({
        'status_code': 200,
        'status': 'success',
        'data': request.json
    })
