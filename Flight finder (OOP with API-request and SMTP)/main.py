import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# setting my origin city for the flight finder
ORIGIN_CITY_IATA = "HAM"

# creating objects from imported classes
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

# setting timeframes for the flight search
tomorrow = dt.datetime.now().date() + dt.timedelta(1)
half_year = dt.datetime.now() + dt.timedelta(days=(6 * 30))

# getting destination data
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_iata()
    sheet_data = data_manager.get_destination_data()

# getting flight options for destination data and send a notification if it is within the specified price range
for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=half_year
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_notification(flight_price=flight.price,
                                               flight_destination=flight.destination_city,
                                               destination_iata=flight.destination_airport,
                                               origin_city=flight.origin_city,
                                               origin_iata=flight.origin_airport,
                                               outbound_date=flight.out_date,
                                               inbound_date=flight.return_date,
                                               amount_of_stopovers=flight.stop_overs,
                                               via_city=flight.via_city
                                                )



