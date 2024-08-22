def process_data(df):
    """Process the merged DataFrame for model training."""
    # Convert categorical activity level to numerical
    df['activity_level'] = df['activity_level'].map({'low': 0, 'moderate': 1, 'high': 2})
    
    # Create features and labels
    features = df[['heart_rate', 'sleep_duration', 'activity_level', 'memory_score', 'attention_score']]
    labels = (df['problem_solving_score'] > 70).astype(int)  # Binary classification
    
    return features, labels

features, labels = process_data(data)
print(features.head(), labels.head())
