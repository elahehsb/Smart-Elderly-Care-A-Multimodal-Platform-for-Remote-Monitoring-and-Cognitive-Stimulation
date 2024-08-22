def collect_cognitive_data():
    """Simulate the collection of cognitive exercise data."""
    memory_score = random.randint(60, 100)
    attention_score = random.randint(50, 100)
    problem_solving_score = random.randint(40, 90)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    return timestamp, memory_score, attention_score, problem_solving_score

def store_cognitive_data(data):
    """Store collected cognitive data in a local SQLite database."""
    conn = sqlite3.connect('elderly_care.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS CognitiveData
                      (timestamp TEXT, memory_score INTEGER, attention_score INTEGER, problem_solving_score INTEGER)''')
    
    cursor.execute('''INSERT INTO CognitiveData (timestamp, memory_score, attention_score, problem_solving_score)
                      VALUES (?, ?, ?, ?)''', data)
    
    conn.commit()
    conn.close()

# Collect and store data every hour (simulated by a loop with sleep)
for _ in range(10):  # Simulate 10 hours of data collection
    data = collect_cognitive_data()
    store_cognitive_data(data)
    time.sleep(1)  # Sleep for a second to simulate real-time collection
