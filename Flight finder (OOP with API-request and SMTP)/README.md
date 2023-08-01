# Flight Finder Project
Do you also feel like just going somewhere new, as long as the flights are cheap? Or maybe you'd like to visit friends or family abroad, and are flexible to travel when prices are low? 
Then I have the program for you. 
I built a flight finder that sends you a notification if there's a flight available from your list of desired destinations, at your desired price, in your desired timeframe. Never miss out on a deal again ☀🐱‍🐉🌴✈🌍


### What files are needed?
All the files that you need are included in the project folder. They are:
    1. main.py  -- This is the file you need to run
    2. data_manager.py -- This file contains a class that gets and/or the destination information from Sheety (location, IATA-code, maximum price of flight)
    3. flight_data.py -- This file contains a class that stores flight data from the flight search
    4. flight_search.py -- This file contains a class that searches for flights and gets the data, and fills in missing IATA-codes if necessary
    5. notification_manager.py -- This file contains a class that is responsible for sending notifications with the deal flight details, if a good deal is found

For the requirements, check requirements.txt

### What other things do I need to run this?
    1. Sheety API account (https://sheety.co/)
    2. Kiwi / Tequila account (https://partners.kiwi.com/)
    3. Any e-mail account (that you can pass in in the notification manager)
    4. You can adjust parameters to your personal preference to get actual useful results (like your origin city, and your email. For details, check the API documentation on https://tequila.kiwi.com/portal/docs/tequila_api/locations_api.)
    5. If you would like to run this program automatically, for example daily, you could run it from the cloud.


