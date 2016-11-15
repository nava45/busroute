from flask import request
import os
import sys
import traceback

from flask_restful import reqparse, abort, Api, Resource
import ujson


class RegisterBusRoute(Resource):
    def get(self):
        return "registering busroute"

    def post(self):

        try:
            json_data = request.get_json(force=True)
        except Exception:
            return "Malformed Payload Error: Please check the payload format", 500


class QueryRoutes(Resource):
    def get(self):
        return "bus route search"

    def post(self):

        try:
            json_data = request.get_json(force=True)
        except Exception:
            return "Malformed Payload Error: Please check the payload format", 500


