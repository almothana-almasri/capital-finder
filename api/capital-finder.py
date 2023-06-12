from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 

class handler(BaseHTTPRequestHandler):
    """
    Usage:
    1. To get the capital of a country, append "?country=<country_name>" to the URL.
    2. To get the country associated with a capital, append "?capital=<capital_name>" to the URL.
    """

    def do_GET(self):
        """
        Handles the GET request and sends the response.
        """
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        my_dict = dict(query_list)

        if 'country' in my_dict:
            country = my_dict.get('country')
            url = 'https://restcountries.com/v3.1/name/'
            res = requests.get(url+country)
            data = res.json() 
            capital = data[0]['capital'][0]              
            message = f'The capital of {country} is {capital}'
        
        elif 'capital' in my_dict:
            capital = my_dict.get('capital')
            url = 'https://restcountries.com/v3.1/capital/'
            res = requests.get(url+capital)
            data = res.json()
            country = data[0]['name']['common']
            message = f'The country of {capital} is {country}'
   
        else:
            message = 'You can append /capital-finder?country=Chile to the URL of the website to test it'
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
    