########################################################################################################################################################################
# Name: Will Padgett, Alex Carnes                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, carnesas@mail.uc.edu                                                                                                                   #
# Assignment Number: Assignment 10                                                                                                                                     #
# Due Date:   11/14/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: This assignment executes an API call using a URL.                                                                               #                                                                                                                              
# Brief Description of what this module does: This module creates the APIDataHandler class to interect with the Alpha Vantage API to retrieve and process stock data.  #                                                                                         
#                                                                                                                                                                      #
# Citations: W3 Schools                                                                                                                                                #
# Anything else that's relevant:                                                                                                                                       #
# #api.py                                                                                                                                                              #
########################################################################################################################################################################

import requests
import csv


class APIDataHandler:
    
    """
    A handler for interacting with the Alpha Vantage API to retrieve and process stock data.

    Attributes
     api_key str: The API key required to authenticate requests to Alpha Vantage.
     base_url str: The base URL for Alpha Vantage API requests.
    """
    
    def __init__(self):
        """
        Initialize the APIDataHandler with default parameters for accessing stock data.

        @Attributes
        api_key str: The API key for authenticating with the Alpha Vantage API.
        base_url str: The base URL for the Alpha Vantage API endpoint.
        function str: The specific API function to call.
        symbol str: The stock symbol for which data is being fetched.
        interval str: The time interval for the data (default is '5min').
        outputsize str: The amount of data to retrieve .
        """
        self.api_key = "CAYQJI56NU207574" 
        self.base_url = 'https://www.alphavantage.co/query'
        self.function = 'TIME_SERIES_INTRADAY'
        self.symbol = 'AAPL'
        self.interval = '5min'
        self.outputsize = 'compact'
        

    def get_data(self, datatype='json'):
        """
        Fetch data from the Alpha Vantage API based on specified parameters.

        @Param
        function str: The specific API function to call (e.g., 'TIME_SERIES_INTRADAY').
        symbol str: The stock symbol for which data is being fetched.
        interval str: The time interval for the data.
        outputsize str: The amount of data to retrieve ('compact' or 'full').
        datatype str: The data format to be returned ('json' or 'csv').

        @Return
        dict or str: The response from the API, in JSON format (parsed as a dictionary) or CSV format (as a string).
        """
        
        params = {
            'function': self.function,
            'symbol': self.symbol,
            'interval': self.interval,
            'apikey': self.api_key,
            'outputsize': self.outputsize,
            'datatype': datatype
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        if datatype == 'csv':
            return response.text
        return response.json()

    def parse_data(self, data):
        """
        Parse JSON data retrieved from the Alpha Vantage API.

        @Param:
        data dict: The JSON data returned from the API.

        @Return
        list: A list of dictionaries containing the parsed time series data.
        """
        time_series_key = 'Time Series (5min)'
        time_series = data.get(time_series_key, {})
        
        parsed_data = []
        for timestamp, values in time_series.items():
            record = {'timestamp': timestamp}
            record.update(values)
            parsed_data.append(record)
        
        return parsed_data

    def print_summary(self, data):
        """
        Print a summary of interesting data to the console, including the latest data point and highest price in the series.

        @Param:
        data list: The parsed list of time series data.
        symbol: String is the stock being displayed
        """
        if not data:
            print("No data available to summarize.")
            return

        latest_data = data[0]
        max_close_price = max(float(item['4. close']) for item in data)

        print(f"--- {self.symbol} Stock Data Summary ---")
        print(f"Most recent data (timestamp: {latest_data['timestamp']}):")
        print(f"  Open: {latest_data['1. open']}")
        print(f"  High: {latest_data['2. high']}")
        print(f"  Low: {latest_data['3. low']}")
        print(f"  Close: {latest_data['4. close']}")
        print(f"Highest closing price in the series: {max_close_price}")

    def save_to_csv(self, data, filename= 'Stock_data.csv'):
        """
        Save data to a CSV file.

        @Param:
        data list: The data to save, expected to be a list of dictionaries.
        filename str: The name of the CSV file to save the data to (default is 'output.csv').

        @Return
        None
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data[0].keys())  
            for entry in data:
                writer.writerow(entry.values())
        print(f"Data saved to {filename}")
