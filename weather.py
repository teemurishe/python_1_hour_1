import pyowm #Importing necessary module
#documentation and Youtube guides)
from colorama import init #importing a package for Windows
from colorama import Fore, Back, Style #importing necessary packages

api_key = pyowm.OWM('26177363c268ee1d29d88a3aa230a3d8') #Getting api key
place = input('Enter place to get weather information: ') #Getting place
observation = api_key.weather_at_place(place) #Serching information
weather_info = observation.get_weather() #Highlighting weather from data
temp_info = weather_info.get_temperature('celsius')['temp'] #Getting temperature
detailed_status = weather_info.get_detailed_status() #Getting sky status
print('The temperature is ', temp_info, ' degrees Celsius', sep = '') #Outputting temperature
print('The status is ', detailed_status, sep = '') #Outputting sky status
