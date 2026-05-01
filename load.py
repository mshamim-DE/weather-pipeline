import sqlite3
from transform import transform_weather

def load_weather(city, latitude, longitude):
    print(f"Loading data for {city} into database...")

    # Step 1 - Get clean data from transform
    df = transform_weather(city, latitude, longitude)

    # Step 2 - Connect to database (creates file if not exists)
    conn = sqlite3.connect("weather.db")

    # Step 3 - Save DataFrame into database table
    df.to_sql("weather", conn, if_exists="append", index=False)

    # Step 4 - Close connection
    conn.close()

    print(f"Data loaded successfully! {len(df)} rows saved.")

# Run it
load_weather("Delhi", 28.6139, 77.2090)