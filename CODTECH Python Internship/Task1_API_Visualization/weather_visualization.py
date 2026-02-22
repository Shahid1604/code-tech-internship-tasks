import requests
import matplotlib.pyplot as plt

# Replace with your own OpenWeatherMap API key if needed
API_KEY = "YOUR_API_KEY_HERE"
CITY = "Mumbai"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Basic safety check
if "list" not in data:
    print("API Error:", data)
    raise SystemExit(1)

dates, temps = [], []

for item in data["list"][:8]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])

plt.figure(figsize=(10,5))
plt.plot(dates, temps, marker='o')
plt.title(f"Weather Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
