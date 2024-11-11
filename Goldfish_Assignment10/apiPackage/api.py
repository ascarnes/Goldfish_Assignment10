import requests
import csv

class APIDataHandler:
    """
    A handler for interacting with the Alpha Vantage API to retrieve and process stock data.

    Attributes
     api_key str: The API key required to authenticate requests to Alpha Vantage.
     base_url str: The base URL for Alpha Vantage API requests.
    """
    
    def __init__(self, api_key):
        """
        Initialize the API client with the provided API key.

        @Param
        api_key (str): The API key used for authenticating requests to the Alpha Vantage API.
        """
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    def get_data(self, function, symbol, interval='5min', outputsize='compact', datatype='json'):
        """
        Fetch data from the Alpha Vantage API based on specified parameters.

        @Param
        function str: The specific API function to call (e.g., 'TIME_SERIES_INTRADAY').
        symbol str: The stock symbol for which data is being fetched.
        interval str: The time interval for the data (default is '5min').
        outputsize str: The amount of data to retrieve ('compact' or 'full').
        datatype str: The data format to be returned ('json' or 'csv').

        @Return
        dict or str: The response from the API, in JSON format (parsed as a dictionary) or CSV format (as a string).
        """
        params = {
            'function': function,
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': outputsize,
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
        """
        if not data:
            print("No data available to summarize.")
            return

        latest_data = data[0]
        max_close_price = max(float(item['4. close']) for item in data)

        print("\n--- Stock Data Summary ---")
        print(f"Most recent data (timestamp: {latest_data['timestamp']}):")
        print(f"  Open: {latest_data['1. open']}")
        print(f"  High: {latest_data['2. high']}")
        print(f"  Low: {latest_data['3. low']}")
        print(f"  Close: {latest_data['4. close']}")
        print(f"Highest closing price in the series: {max_close_price}")

    def save_to_csv(self, data, filename):
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
