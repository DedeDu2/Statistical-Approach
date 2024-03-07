import numpy as np

def detect_anomalies_zscore(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 3
    anomalies = []
    for value in data:
        z_score = (value - mean) / std_dev
        if np.abs(z_score) > threshold:
            anomalies.append(value)
    return anomalies

# Example usage:
data = [10, 15, 12, 18, 5, 20, 25, 30, 35, 40, 100]
anomalies = detect_anomalies_zscore(data)
print("Anomalies:", anomalies)
