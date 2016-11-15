from flask import request
import os
import sys
import traceback

from flask_restful import reqparse, abort, Api, Resource
import ujson

from busroute.models import store_routes, lookup_station


class RegisterBusRoute(Resource):
    def get(self):
        return "registering busroute"

    def post(self):
        '''
        Assuming the input data format
        '{"routes": ["1 2 3 4 5", "2 3 4 5", "5 6 7 8"], "tot_routes": 3}'
        :return:
        '''
        try:
            json_data = request.get_json(force=True)
            tot_bus_routes = json_data['tot_routes']
            routes_list = json_data['routes']
            assert len(routes_list) == tot_bus_routes
            for bus_route in routes_list:
                store_routes(bus_route)
            return True, 201
        except Exception as e:
            return str(e), 500


class QueryRoutes(Resource):
    def get(self):
        try:
            dep_id = int(request.args.get('dep_id'))
            arr_id = int(request.args.get('arr_id'))
            is_succ, route = lookup_station(arr_id, dep_id)
            return {
                "dep_sid": dep_id,
                "arr_sid": arr_id,
                "direct_bus_route": is_succ
            }, 200
        except Exception as e:
            return str(e), 500

    def post(self):

        try:
            json_data = request.get_json(force=True)
            return None, 201
        except Exception:
            return "Malformed Payload Error: Please check the payload format", 500


