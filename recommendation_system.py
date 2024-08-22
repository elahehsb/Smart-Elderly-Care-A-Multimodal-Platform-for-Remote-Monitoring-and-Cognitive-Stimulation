def generate_recommendation(row):
    """Generate personalized recommendations based on sensor data."""
    if row['activity_level'] == 0:  # low activity level
        return "Increase physical activity."
    if row['sleep_duration'] < 5:  # poor sleep
        return "Consider sleep improvement strategies."
    if row['attention_score'] < 60:  # low attention
        return "Encourage attention-improving cognitive exercises."
    
    return "Continue current care plan."

# Example application to the dataset
data['recommendation'] = data.apply(generate_recommendation, axis=1)
print(data[['timestamp', 'recommendation']].head())
