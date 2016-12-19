"""Views to handle all api requests."""
import json
import requests

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
    """View to handle sending of mails."""
    dispatcher.send_email(request.json)
    return json.dumps({
        'status_code': 200,
        'status': 'sent',
        'msg': "I see you",
        'data': request.json
    })
