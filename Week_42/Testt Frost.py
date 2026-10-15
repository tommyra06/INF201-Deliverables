import os
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Reading the client ID from a local file
client_path = os.path.expanduser("~/Documents/client.txt")
with open(client_path, encoding="utf-8") as client_file:
    client_id = client_file.read().strip()

endpoint = "https://frost.met.no/observations/v0.jsonld"


def fetch_temperature_data(year):
    """Helper function to fetch daily mean temperature for a specific year."""
    parameters = {
        "sources": "SN17850",
        "elements": "mean(air_temperature P1D)",
        "referencetime": f"{year}-01-01/{year}-12-31",
    }
    response = requests.get(
        endpoint, params=parameters, auth=(client_id, ""), timeout=30
    )

    if response.status_code == 200:
        rows = []
        response_data = response.json()
        for entry in response_data.get("data", []):
            for observation in entry.get("observations", []):
                rows.append({
                    "datetime": entry["referenceTime"],
                    f"temperature_{year}": observation["value"],
                })

        df = pd.DataFrame(rows)
        df["datetime"] = pd.to_datetime(df["datetime"])

        # Extract month-day (MM-DD) to align both years on the same X-axis
        df["day_of_year"] = df["datetime"].dt.strftime("%m-%d")
        return df[["day_of_year", f"temperature_{year}"]].drop_duplicates(
            "day_of_year"
        )
    else:
        print(f"Error fetching {year} data: {response.status_code}")
        return None


# Fetch observations for both years
df_1925 = fetch_temperature_data(1925)
df_2025 = fetch_temperature_data(2025)

if df_1925 is not None and df_2025 is not None:
    # Merge datasets on day of year
    df_comparison = pd.merge(df_1925, df_2025, on="day_of_year").sort_values(
        "day_of_year"
    )

    # 1. Generate Summary Statistics Table
    summary_table = df_comparison[
        ["temperature_1925", "temperature_2025"]
    ].describe()
    summary_table.columns = ["1925 Temperature (°C)", "2025 Temperature (°C)"]

    print("=== Temperature Summary Statistics (1925 vs 2025) ===")
    print(summary_table)

    # 2. Plotting Both Years on a Single Plot
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        df_comparison["day_of_year"],
        df_comparison["temperature_1925"],
        color="tab:blue",
        alpha=0.7,
        linewidth=1.2,
        label="1925",
    )
    ax.plot(
        df_comparison["day_of_year"],
        df_comparison["temperature_2025"],
        color="tab:red",
        alpha=0.8,
        linewidth=1.2,
        label="2025",
    )

    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.set_ylabel("Temperature (°C)", fontsize=11)
    ax.set_xlabel("Date (MM-DD)", fontsize=11)
    ax.set_title(
        "Daily Mean Temperature Comparison in Ås: 1925 vs 2025",
        fontsize=13,
        fontweight="bold",
    )

    # Reduce X-axis tick frequency to avoid label overcrowding
    ax.set_xticks(df_comparison["day_of_year"][::30])
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(title="Year")

    plt.tight_layout()
    plt.show()