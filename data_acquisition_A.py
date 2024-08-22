import random
import time
import sqlite3

def collect_sensor_data():
    """Simulate the collection of sensor data."""
    heart_rate = random.randint(60, 100)
    sleep_duration = random.uniform(4, 8)  # hours
    activity_level = random.choice(['low', 'moderate', 'high'])
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    return timestamp, heart_rate, sleep_duration, activity_level

def store_sensor_data(data):
    """Store collected sensor data in a local SQLite database."""
    conn = sqlite3.connect('elderly_care.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData
                      (timestamp TEXT, heart_rate INTEGER, sleep_duration REAL, activity_level TEXT)''')
    
    cursor.execute('''INSERT INTO SensorData (timestamp, heart_rate, sleep_duration, activity_level)
                      VALUES (?, ?, ?, ?)''', data)
    
    conn.commit()
    conn.close()

# Collect and store data every hour (simulated by a loop with sleep)
for _ in range(10):  # Simulate 10 hours of data collection
    data = collect_sensor_data()
    store_sensor_data(data)
    time.sleep(1)  # Sleep for a second to simulate real-time collection
