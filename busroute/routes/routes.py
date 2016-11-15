from busroute.appconfig import sourcer_api
from busroute.routes.resources import RegisterBusRoute, QueryRoutes


# Response Receiver Sample
sourcer_api.add_resource(QueryRoutes, '/api/direct')
sourcer_api.add_resource(RegisterBusRoute, '/api/register')
