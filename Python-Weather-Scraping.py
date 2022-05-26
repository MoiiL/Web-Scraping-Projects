# Weather scraping using Python from BBC weather website

#importing the required libraries 
import os
import requests      # retrieving the webpages
import json          # converting the API to a json format

from urllib.parse import urlencode     #provide structure to the API url

import numpy as np
import pandas as pd
import re


test-city = input('Enter a City: ')
location-url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode ({
     'api-key' : 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
     's' : test-city ,
     'stack' : 'aws' ,
     'locale' : 'en' ,
     'filter' : 'international' ,
     'place-types' : 'settlement, airport, district' ,
     'order' : 'importance' , 
     'a' : 'true' ,
     'format' : 'json'
})
location-url

result = requests.get(location-url).json()
result

#printing the location id

result['response']['results']['results'][0]['id']

# A function to output location ID by taking any city name 

def getlocationid(city):
  city = city.lower()
  location-url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode ({
     'api-key' : 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
     's' : city ,
     'stack' : 'aws' ,
     'locale' : 'en' ,
     'filter' : 'international' ,
     'place-types' : 'settlement, airport, district' ,
     'order' : 'importance' , 
     'a' : 'true' ,
     'format' : 'json'
   })
  result = requests.get(location-url).json()
  locationid = result['response']['results']['results'][0]['id']
  return locationid
 
