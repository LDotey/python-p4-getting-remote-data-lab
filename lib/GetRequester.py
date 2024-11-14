import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        # URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        # response = requests.get(URL)
        return response.content
        pass

    def load_json(self):

        # url = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.jsonLinks'
        # print(url)
        response = requests.get(self.url)
        return response.json()
        pass



#     All work should be completed in lib/GetRequester.py. 
# Use the previous code-along on getting data from 
# APIs as a reference when building out your class.

# Start by creating a GetRequester class. 
# This class should be able to initialize with a string URL.

# The GetRequester class should have a get_response_body method 
# that sends a GET request to the URL passed in on initialization. 
# This method should return the body of the response.

# The GetRequester class should have a load_json method that 
# should use get_response_body to send a request, 
# then return a Python list or dictionary made up of data converted 
# from the response of that request.

# The tests in this lab will use your code to send 
# a request for some JSON data, located at 
# https://learn-co-curriculum.github.io/json-site-example/endpoints/people.jsonLinks 
# to an external site.. 
# Read the test error messages for additional 
# as you work for additional information. 
# Don't forget to import the necessary Python modules and classes!