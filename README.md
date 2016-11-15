# busroute

### Problem

We are adding a new bus provider to our system. In order to implement a very specific requirement of this bus provider our system needs to be able to filter direct connections. We have access to a weekly updated list of bus routes in form of a bus route data file. As this provider has a lot of long bus routes, we need to come up with a proper service to quickly answer if two given stations are connected by a bus route.

### Task

The bus route data file provided by the bus provider contains a list of bus routes. These routes consist of an unique identifier and a list of stations (also just unique identifiers). A bus route connects its list of stations.

Your task is to implement a micro service which is able to answer whether there is a bus route providing a direct connection between two given stations. Note: The station identifiers given in a query may not be part of any bus route!

### Bus Route Data

The first line of the data gives you the number N of bus routes, followed by N bus routes. For each bus route there will be one line containing a space separated list of integers. This list contains at least three integers. The first integer represents the bus route id. The bus route id is unique among all other bus route ids in the input. The remaining integers in the list represent a list of station ids. A station id may occur in multiple bus routes, but can never occur twice within the same bus route.

You may assume 100,000 as upper limit for the number of bus routes, 1,000,000 as upper limit for the number of stations, and 1,000 as upper limit for the number of station of one bus route. Therefore, your internal data structure should still fit into memory on a suitable machine.

Note: The bus route data file will be a local file and your service will get the path to file as the first command line argument. Your service will get restarted if the file or its location changes.

### REST API

Your micro service has to implement a REST-API supporting a single URL and only GET requests. It has to serve http://localhost:8088/api/direct?dep_sid={}&arr_sid={}. The parameters dep_sid (departure) and arr_sid (arrival) are two station ids (sid) represented by 32 bit integers.

#### The response has to be a single JSON Object:

{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "dep_sid": {
      "type": "integer"
    },
    "arr_sid": {
      "type": "integer"
    },
    "direct_bus_route": {
      "type": "boolean"
    }
  },
  "required": [
    "dep_sid",
    "arr_sid",
    "direct_bus_route"
  ]
}
The direct_bus_route field has to be set to true if there exists a bus route in the input data that connects the stations represented by dep_sid and arr_sid. Otherwise direct_bus_route must be set to false.

### Example Data

#### Bus Routes Data File:

3    
0 0 1 2 3 4    
1 3 1 6 5     
2 0 6 4      

#### Query:

http://localhost:8088/api/direct?dep_sid=3&arr_sid=6
#### Response:

{
    "dep_sid": 3,
    "arr_sid": 6,
    "direct_bus_route": true
}

## Solution:

. It is a flask-restful service.
. It contains volatile data store to hold all bus route information
. The bus route informations are connected by a linked list representation
. You can post the input data

### Run the flask service:

`python run.py` (default running in 5000 port)

### Post inputs:
`
curl -X POST "http://localhost:5000/api/register" -d '{"routes": ["1 1 2 3 4 5", "2 3 4 5", "5 6 7 8"], "tot_routes": 3}' -vvv
`
 - 3 routes are posted, it should match with the total routes 
 - Each route's first item is route_id, remaining elements are station ids

### Query the api:

`
curl -X GET "http://localhost:5000/api/direct?dep_id=5&arr_id=7" -vvv
`

##### response

`
{
    "arr_sid": 7, 
    "dep_sid": 5, 
    "direct_bus_route": false
}

`

