########################################################################################################################################################################
# Name: Will Padgett, Alex Carnes                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, carnesas@mail.uc.edu                                                                                                                   #
# Assignment Number: Assignment 10                                                                                                                                     #
# Due Date:   11/14/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: This assignment executes an API call using a URL.                                                                               #                                                                                                                              
# Brief Description of what this module does: Calls the API data handler class and sets the settings.                                                                  #                          
#                                                                                                                                                                      #
# Citations: W3 Schools                                                                                                                                                #
# Anything else that's relevant:                                                                                                                                       #
# #main.py                                                                                                                                                             #
########################################################################################################################################################################


from apiPackage.api import APIDataHandler


if __name__ == "__main__" :
        
    api_key = ""
    function = 'TIME_SERIES_INTRADAY'
    symbol = 'AAPL'
    interval = '5min'
    outputsize = 'compact'
 
    handler = APIDataHandler(api_key)
    raw_data = handler.get_data(function=function, symbol=symbol, interval=interval, outputsize=outputsize)
 
    # Parse data
    parsed_data = handler.parse_data(raw_data)
 
    # Print interesting data summary
    handler.print_summary(parsed_data, symbol)
 
    # Save data to CSV
    handler.save_to_csv(parsed_data, filename='stock_data.csv')

 

