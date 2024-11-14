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
        
   
 
    handler = APIDataHandler()
    # Fetch data
    raw_data = handler.get_data()         
    # Parse data
    parsed_data = handler.parse_data(raw_data)  
     # Print summary
    handler.print_summary(parsed_data)     
    # Save data to CSV

    handler.save_to_csv(parsed_data)       
 

