import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read your personal Frost client ID from client.txt.
client_id_path = os.path.expanduser("~/Documents/client.txt")
with open(client_id_path, encoding="utf-8") as client_file:
    client_id = client_file.read().strip()

# Define the observations endpoint and request parameters.
endpoint = "https://frost.met.no/observations/v0.jsonld"

parameters = {
    "sources": "SN17850",
    "elements": "mean(air_temperature P1D)",
    "referencetime": "2025-01-01/2025-12-31",
}

response = requests.get(endpoint, auth=(client_id, ""), params=parameters)
response.raise_for_status()
observations = response.json()["data"]

daily_temperatures = [
    {"date": item["referenceTime"], "temperature": observation["value"]}
    for item in observations
    for observation in item["observations"]
]
if not daily_temperatures:
    raise ValueError("Frost returned no daily air-temperature observations.")

temperatures = pd.DataFrame(daily_temperatures)
temperatures["date"] = pd.to_datetime(temperatures["date"])
temperatures = temperatures.sort_values("date")

summary = temperatures["temperature"].agg(["mean", "median", "min", "max"])
summary_table = summary.to_frame(name="Temperature (°C)").rename_axis("Statistic")
print("\nDaily mean air temperature in 2025")
print(summary_table.to_string(float_format=lambda value: f"{value:.2f}"))

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    temperatures["date"],
    temperatures["temperature"],
    color="tab:blue",
    linewidth=1.5,
)
ax.set(
    title="Daily Mean Air Temperature at SN17850 (2025)",
    xlabel="Date",
    ylabel="Temperature (°C)",
)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.grid(True, linestyle="--", alpha=0.5)
fig.tight_layout()
plt.show()
