
# Weather Check App

## Setting up the Project

1. Create a project folder and initialize a Python virtual environment:

   ```bash
   mkdir weather_app
   cd weather_app
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install the necessary libraries, including requests and argparse:

   ```bash
   pip install requests argparse

3. Activate/Deactivate the Virtual Environment:

   * To activate the virtual environment:

      ```bash
      source venv/bin/activate  # On Windows: venv\Scripts\activate

   * To deactivate the virtual environment:

      ```bash
      deactivate

## Description

* The Weather Check App is a command-line interface (CLI) application that allows you to check the weather for a specific city and manage your favorite cities. Here's how you can use it:

      ```bash
      usage: weather_check_app.py [-h] [--unit {C,F}] [--addfavorites] [--removefavorites] [--listfavorites] [--getweatherfavorites] [city]
   
      Weather Checking Application

      positional arguments:
      city                  City for which you want to check the weather

      options:
      -h, --help             show this help message and exit
      --unit {C,F}           Temperature unit (Celsius or Fahrenheit)
      --addfavorites         Add this city to favorites
      --removefavorites      Remove the city from favorites
      --listfavorites        List the favorite cities
      --getweatherfavorites  Display weather for favorite cities

## Usage

* To check the weather for a specific city, run:

   ```bash
   python weather_check_app.py "City Name"
You can specify the temperature unit (Celsius or Fahrenheit) using the --unit option.

* To add a city to your list of favorite cities, use the --addfavorites option:

   ```bash
   python weather_check_app.py "City Name" --addfavorites
* To remove a city from your list of favorite cities, use the --removefavorites option:

   ```bash
   python weather_check_app.py "City Name" --removefavorites
* To list your favorite cities, use the --listfavorites option:

   ```bash
   python weather_check_app.py --listfavorites
* To display the weather for your favorite cities, use the --getweatherfavorites option:

   ```bash
   python weather_check_app.py --getweatherfavorites
* Enjoy using the Weather Check App to keep track of the weather for your favorite cities!
