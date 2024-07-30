import matplotlib.pyplot as plt

import requests

# Define the location coordinates
latitude = 39.7456
longitude = -97.0892

# Get the grid points
response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
data = response.json()
grid_id = data['properties']['gridId']
grid_x = data['properties']['gridX']
grid_y = data['properties']['gridY']

# Get the forecast
forecast_url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

# Print the forecast
for period in forecast_data['properties']['periods']:
    print(f"{period['name']}: {period['detailedForecast']}")


x_cords = [1] #add points by making a comma and an integer

y_cords = [1] #add points by making a comma and an integer


x_sum = sum(x_cords)

y_sum = sum(y_cords)

slope = y_sum/x_sum
y_intercept = 0
for i in range(1, len(x_cords)):  
  y_intercept = y_intercept + (y_cords[i-1] - (slope * x_cords[i-1]))

y = [(slope * x) + y_intercept for x in x_cords] 

plt.plot(x_cords, y_cords, label='Original Data')
plt.plot(x_cords, y, label='MAD Line')

for x in x_cords:
  plt.scatter(x, y_cords[x_cords.index(x)], color='red', label=('Point',x))

plt.legend()
plt.show()
