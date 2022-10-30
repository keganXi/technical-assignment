# api/google_geocode.py

from technical_assignment.settings.base import GOOGLE_API_KEY
import requests


class GeocodeClient:


    def __init__(self, address):
        """
            NOTE:
                - convert addresses (like a street address) into geographic
                  coordinates (like latitude and longitude).

            @params
                address - home address.
        """
        self.api_key = GOOGLE_API_KEY # google api key
        self.api_response = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.api_key}')
        self.api_response_dict = self.api_response.json()
        self.status = self.api_response_dict['status']
    

    def get_location(self):
        """
            returns string containing latitude and longitude.
        """
        location = ",".join(
            [str(self.api_response_dict['results'][0]['geometry']['location']['lat']),
                str(self.api_response_dict['results'][0]['geometry']['location']['lng'])])
        return location 
