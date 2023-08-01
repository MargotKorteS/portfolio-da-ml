import requests
from flight_data import FlightData

KIWI_URL = "https://tequila-api.kiwi.com"

KIWI_API_EMAIL = "my-private-email"
KIWI_API_KEY = "my-private-api-key"

SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    """This class searches for available flights with the Kiwi/Tequila API."""
    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_name):
        """Gets missing IATA codes"""
        location_endpoint = f"{KIWI_URL}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        for city in city_name:
            fs_params = {
            "term": city_name,
            "location_types": "city",
        }
            response = requests.get(url=location_endpoint, params=fs_params, headers=headers)
            response.raise_for_status()
            flight_query = response.json()["locations"]
            code = flight_query[0]["code"]
            self.city_codes.append(code)
        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Gets flights within set parameters and saves flight data to FlightData-class"""
        headers = {"apikey": KIWI_API_KEY}
        flight_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "EUR",
            "max_stopovers": 0,
        }

        response = requests.get(url=SEARCH_API_ENDPOINT, headers=headers, params=flight_params)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code}: {data['price']}")
        except IndexError:
            print(f"No flights found for {destination_city_code} with current parameters.")
            return None

        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data


