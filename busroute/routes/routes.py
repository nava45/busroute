from busroute.appconfig import sourcer_api
from busroute.routes.resources import RegisterBusRoute


# Response Receiver Sample
sourcer_api.add_resource(RegisterBusRoute, '/api/direct')
