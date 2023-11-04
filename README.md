Setting up the Project:

Start by creating a project folder and initializing a Python virtual environment.

mkdir weather_app
cd weather_app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Required Libraries:

Install the necessary libraries, including requests, argparse.
-- pip install requests argparse

Actvating/Deactvating Virtual Environment
 --  venv\Scripts\activate
 --  deactivate

Description for using the Weather Check App in Command Line Interface:

usage: weather_check_app.py [-h] [--unit {C,F}] [--addfavorites]
                            [--removefavorites] [--listfavorites]
                            [--getweatherfavorites]
                            [city]

Weather Checking Application

positional arguments:
  city                  City for which you want to check the weather

options:
  -h, --help             show this help message and exit
  --unit {C,F}           Temperature unit (Celsius or Fahrenheit)
  --addfavorites         Add this city to favorites
  --removefavorites      Remove the city from favorites
  --listfavorites        List the favorites cities
  --getweatherfavorites  Display weather for favorite cities