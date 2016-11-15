from flask import Flask, got_request_exception

import logging
import os

from flask_restful import Api


# app
sourcer_app = Flask(__name__)
sourcer_api = Api(sourcer_app)


# Routes
from routes import routes


def run_server():
    sourcer_app.run('0.0.0.0', '5000')

if __name__ == '__main__':
    run_server()

