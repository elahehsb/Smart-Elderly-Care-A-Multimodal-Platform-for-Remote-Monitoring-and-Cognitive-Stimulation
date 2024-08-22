def fetch_data():
    """Retrieve and merge sensor and cognitive data from the database."""
    conn = sqlite3.connect('elderly_care.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM SensorData''')
    sensor_data = cursor.fetchall()
    
    cursor.execute('''SELECT * FROM CognitiveData''')
    cognitive_data = cursor.fetchall()
    
    conn.close()
    
    # Convert data to DataFrames (optional, depending on processing requirements)
    import pandas as pd
    sensor_df = pd.DataFrame(sensor_data, columns=['timestamp', 'heart_rate', 'sleep_duration', 'activity_level'])
    cognitive_df = pd.DataFrame(cognitive_data, columns=['timestamp', 'memory_score', 'attention_score', 'problem_solving_score'])
    
    # Merge data on timestamp
    merged_df = pd.merge(sensor_df, cognitive_df, on='timestamp')
    
    return merged_df

data = fetch_data()
print(data.head())
