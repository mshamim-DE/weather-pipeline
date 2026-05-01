import pandas as pd
from extract import fetch_weather

def transform_weather(city, latitude, longitude):
    print(f"Transforming data for {city}...")

    # Step 1 - Get raw data
    raw = fetch_weather(city, latitude, longitude)

    # Step 2 - Build the table with hourly data
    df = pd.DataFrame({
        "time"      : raw["hourly"]["time"],
        "humidity"  : raw["hourly"]["relativehumidity_2m"],
        "radiation" : raw["hourly"].get("direct_radiation", 0),
    })

    # Step 3 - Add current weather columns
    df["city"]          = city
    df["temperature"]   = raw["current_weather"]["temperature"]
    df["windspeed"]     = raw["current_weather"]["windspeed"]
    df["winddirection"] = raw["current_weather"]["winddirection"]
    df["weathercode"]   = raw["current_weather"]["weathercode"]
    df["is_day"]        = raw["current_weather"]["is_day"]

    # Step 4 - Convert time to proper datetime
    df["time"] = pd.to_datetime(df["time"])

    # Step 5 - Reorder columns neatly
    df = df[[
        "city",
        "time",
        "temperature",
        "windspeed",
        "winddirection",
        "weathercode",
        "is_day",
        "humidity",
        "radiation"
    ]]

    print("Transformation complete!")
    print(df.head())
    return df

# Run it
transform_weather("Delhi", 28.6139, 77.2090)