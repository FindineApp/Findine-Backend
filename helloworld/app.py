from chalice import Chalice

from random import randint
import googlemaps
import json
import pprint
#import xlsxwriter
import time
#import os



app = Chalice(app_name='helloworld')

def getResturant():
    # Define the API Key.
    API_KEY = ''

    # Define the Client
    gmaps = googlemaps.Client(key = API_KEY)

    # Do a simple nearby search where we specify the location
    # in lat/lon format, along with a radius measured in meters
    places_result  = gmaps.places_nearby(location='49.1681184087879, -123.1362330541569', radius = 3000, open_now =False , type = 'restaurant')

    time.sleep(3)

    place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

    luckyNum = randint(0,10)
    print(places_result['results'][luckyNum]['name'])
    return(places_result['results'][luckyNum]['name'])
    
#coordinates formate: '49.1681184087879, -123.1362330541569'
def getResturant(coordinates):
    # Define the API Key.
    API_KEY = 'AIzaSyADetO8a2_rTpsKYG6HGWnSElmlspiKi_8'

    # Define the Client
    gmaps = googlemaps.Client(key = API_KEY)

    # Do a simple nearby search where we specify the location
    # in lat/lon format, along with a radius measured in meters
    places_result  = gmaps.places_nearby(location=coordinates, radius = 3000, open_now =False , type = 'restaurant')
    
    time.sleep(3)

    place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])

    luckyNum = randint(0,10)
    #print(places_result['results'][luckyNum]['name'])
    
    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = places_result['results'][luckyNum]['place_id']

    # make a request for the details.
    places_details  = gmaps.place(place_id= my_place_id)
    return places_details
    #return(places_result['results'][luckyNum]['name'])


@app.route('/')
def index():
    a = getResturant()
    return {'Your recommened returant': a}
    
   
@app.route('/echo',methods=['POST'])
def echoback():
    request = app.current_request
    message = request.json_body
    result = getResturant(message["Location"])
    return {'Your recommened returant': result}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
