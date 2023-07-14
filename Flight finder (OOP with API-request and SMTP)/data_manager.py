import requests

SHEETY_PRICES_ENDPOINT = "my-private-sheety-api-endpoint"


class DataManager:
# this class gets the destination data saved in Sheety, and allows the IATA-codes to be updated
## The Sheety-file consists of 3 columns: one for destinations, one for IATA-codes and one for the maximum price point.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

