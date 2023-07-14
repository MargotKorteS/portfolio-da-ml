import smtplib

MY_EMAIL = "my-private-email"
MY_PASSWORD = "my-private-password"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, flight_price, flight_destination, destination_iata, origin_city, origin_iata, amount_of_stopovers, via_city,
                          outbound_date, inbound_date):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            if amount_of_stopovers == 0:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="any-email",
                                    msg=f"Subject:A flight to {flight_destination} is available \n\n"
                                        f" A flight is available from {origin_city} to {flight_destination} "
                                        f"for {flight_price} euro. \n\n "
                                        f"Departure is on {outbound_date} from {origin_city}, {origin_iata} and return is "
                                        f"on {inbound_date} from {flight_destination}, {destination_iata}.\n\n"
                                        f"You can book the flight via: https://www.google.co.uk/flights?hl=en#flt={origin_iata}.{destination_iata}.{outbound_date}*{destination_iata}.{origin_iata}.{inbound_date}")
            else:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="any-email",
                                    msg=f"Subject:A flight to {flight_destination} is available \n\n"
                                        f" A flight is available from {origin_city} to {flight_destination} "
                                        f"for {flight_price} euro. \n\n "
                                        f"Departure is on {outbound_date} from {origin_city}, {origin_iata} and return is "
                                        f"on {inbound_date} from {flight_destination}, {destination_iata}\n\n"
                                        f"The flight has {amount_of_stopovers} stopovers via {via_city}.\n\n"
                                        f"You can book the flight via: https://www.google.co.uk/flights?hl=en#flt={origin_iata}.{destination_iata}.{outbound_date}*{destination_iata}.{origin_iata}.{inbound_date}")

