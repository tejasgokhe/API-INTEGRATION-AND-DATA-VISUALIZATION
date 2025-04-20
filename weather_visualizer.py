import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#CONFIGURATION
API_KEY = '7774800905323b2953b3c90beadd6475' 
CITY = 'Nagpur'
UNITS = 'metric'
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&units={UNITS}&appid={API_KEY}"

#FETCH WEATHER DATA
response = requests.get(URL)
data = response.json()

print(data)

if data.get("cod") != "200":
    print("Error from API:", data.get("message"))
    exit()

#PARSE THE DATA
dates = []
temperatures = []
humidities = []


for forecast in data['list']:
    dt = datetime.fromtimestamp(forecast['dt'])
    temp = forecast['main']['temp']
    humidity = forecast['main']['humidity']
    
    dates.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)

#PLOT TEMPERATURE TREND
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker="o", color="orange")
plt.title(f"Temperature Trend for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#PLOT HUMIDITY TREND
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=humidities, marker="s", color="blue")
plt.title(f"Humidity Trend for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
