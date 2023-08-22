from geopy.geocoders import Nominatim
from geopy.point import Point
from geopy.distance import geodesic
import pandas as pd
import googlemaps


class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.__geolocator = Nominatim(user_agent='demo_of_gnss_help', timeout=20)
        self.point = Point(self.lat, self.lon)

    def get_separation(self, l):
        l1 = (self.lat, self.lon)
        l2 = (l.lat, l.lon)
        return geodesic(l1, l2).meters

    def get_average_geocode(self, l):
        lat = (self.lat + l.lat) / 2
        lon = (self.lon + l.lon) / 2
        return [lon, lat]

    def get_head(self, l):
        api_key = "AIzaSyBOg3mbFMqox4CbDiYl1Y5uyLYuHCJc_bA"
        client = googlemaps.Client(api_key)

        l1 = (self.lat, self.lon)
        l2 = (l.lat, l.lon)

        a1 = client.elevation([l1])[0]["elevation"]
        a2 = client.elevation([l2])[0]["elevation"]
        return abs(a1 - a2)
    
    
if __name__ == '__main__':
    l1 = Location(1.5782065575090678, 108.62547847458541)
    l2 = Location(34.2253171, -108.9426205)
    print(l1.get_separation(l2))
    print(l1.get_head(l2))