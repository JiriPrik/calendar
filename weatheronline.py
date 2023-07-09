
key = "bb1e3ba8-167d-11ee-8d52-0242ac130002-bb1e3c20-167d-11ee-8d52-0242ac130002"

import arrow
import requests

# Get first hour of today
start = arrow.now().floor('day')

# Get last hour of today
end = arrow.now().ceil('day')

response = requests.get(
  'https://api.stormglass.io/v2/solar/point',
  params={
    'lat': 58.7984,
    'lng': 17.8081,
    'params': ','.join(['uvIndex']),
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp()  # Convert to UTC timestamp
  },
  headers={
    'Authorization': key
  }
)

# Do something with response data.
json_data = response.json()


print(json_data)