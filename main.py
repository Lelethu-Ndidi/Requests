import requests

#Prints the html boiler point
# response=requests.get('https://w3schools.com/python/demopage.htm')
# print(response.text)
# prints the html boiler point in one line
# response=requests.get('https://w3schools.com/python/demopage.htm')
# print(response.content)
# The header information displaying the metadata info
# response=requests.get('https://w3schools.com/python/demopage.htm')
# print(response.headers)

# url='https://v6.exchangerate-api.com/v6/422f2a8448fe972fdcc3eef2/latest/USD'
# Only ptints out the data information(in dictionaries)
# answer=requests.get(url)
# result=answer.json()
# print(result['conversion_rates'])
# toUSD=result['conversion_rates']['USD']
# toBGN=result['conversion_rates']['BGN']
# print(toUSD,toBGN)

# printing out text with all the details, hearder,content and so fourth.
# answer=requests.get(url)
# result=answer.text
# print(result)


url='https://api.openweathermap.org/data/2.5/weather'
weather_key='030cd25c050039857c662f6fcde38ddb'
params1 ={'appid': weather_key,'q':'London,uk','units':'Metric'}
response = requests.get(url,params=params1)
weather=response.json()
print(weather)
print(weather['sys']['country'])


# url='https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=030cd25c050039857c662f6fcde38ddb'
