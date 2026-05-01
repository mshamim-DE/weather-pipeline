import sqlite3

# Connect to database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# ----------------------------
# Query 1 - See all data
# ----------------------------
print("=== ALL DATA (first 5 rows) ===")
cursor.execute("""
    SELECT city, time, temperature, humidity, radiation
    FROM weather
    LIMIT 5
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ----------------------------
# Query 2 - Highest radiation
# ----------------------------
print("\n=== HIGHEST SOLAR RADIATION ===")
cursor.execute("""
    SELECT time, radiation
    FROM weather
    ORDER BY radiation DESC
    LIMIT 3
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ----------------------------
# Query 3 - Most humid hours
# ----------------------------
print("\n=== MOST HUMID HOURS ===")
cursor.execute("""
    SELECT time, humidity
    FROM weather
    ORDER BY humidity DESC
    LIMIT 3
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ----------------------------
# Query 4 - Daytime only
# ----------------------------
print("\n=== DAYTIME HOURS ONLY ===")
cursor.execute("""
    SELECT time, temperature, radiation
    FROM weather
    WHERE is_day = 1
    LIMIT 5
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# High radiation hours
print("\n=== HIGH RADIATION HOURS (Daytime) ===")
cursor.execute("""
    SELECT time, temperature, humidity, radiation
    FROM weather
    WHERE radiation > 400
    ORDER BY radiation DESC
    LIMIT 5
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()