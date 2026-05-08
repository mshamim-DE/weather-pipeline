import psycopg2
import psycopg2.extras
from transform import transform_weather

def load_weather_postgres(city, latitude, longitude):
    print(f"Loading data for {city} into PostgreSQL...")

    # Step 1 - Get clean data
    df = transform_weather(city, latitude, longitude)

    # Step 2 - Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="weather_db",
        user="postgres",
        password="India143"
    )

    cursor = conn.cursor()

    # Step 3 - Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city VARCHAR(100),
            time TIMESTAMP,
            temperature FLOAT,
            windspeed FLOAT,
            winddirection INT,
            weathercode INT,
            is_day INT,
            humidity INT,
            radiation FLOAT
        )
    """)

    # Step 4 - Insert rows
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather (
                city, time, temperature, windspeed,
                winddirection, weathercode, is_day,
                humidity, radiation
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["city"], row["time"], row["temperature"],
            row["windspeed"], row["winddirection"],
            row["weathercode"], row["is_day"],
            row["humidity"], row["radiation"]
        ))

    # Step 5 - Save and close
    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ {city} loaded — {len(df)} rows saved to PostgreSQL!")

# Run it
load_weather_postgres("Delhi", 28.6139, 77.2090)