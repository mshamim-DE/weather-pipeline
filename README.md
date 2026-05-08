# 🌦️ Weather Pipeline

An automated ETL pipeline that collects live weather data 
for Indian cities, transforms it and stores it in a database 
for analysis.

## 🎯 What it Does
- Fetches live weather data from Open-Meteo API
- Cleans and structures the data using Pandas
- Stores 168 hours of hourly data per city in SQLite
- Runs automatically every day via Windows Task Scheduler

## 🛠️ Technologies Used
- Python
- Pandas
- SQLite
- REST API (Open-Meteo)
- Git & GitHub

## 📁 Project Structure
weather_pipeline/
├── extract.py    # Fetches data from API
├── transform.py  # Cleans and reshapes data
├── load.py       # Stores data in database
├── query.py      # SQL queries for analysis
└── weather.db    # SQLite database

## ⚙️ How to Run
1. Install dependencies:
   pip install requests pandas

2. Run the pipeline:
   python load.py

3. Query the data:
   python query.py

## 📊 Sample Queries
```sql
-- Highest solar radiation hours
SELECT time, radiation
FROM weather
ORDER BY radiation DESC
LIMIT 5;

-- Most humid hours
SELECT time, humidity
FROM weather
ORDER BY humidity DESC
LIMIT 5;
```

## 🏙️ Cities Covered
Delhi

## 👨‍💻 Author
mshamim-DE | Learning Data Engineering