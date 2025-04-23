import statistics

# Function to calculate common statistics
def calculate_statistics(data):
    mean = statistics.mean(data)  # Average
    median = statistics.median(data)  # Middle value

    # Handle case with no unique mode
    try:
        mode = statistics.mode(data)  # Most common value
    except statistics.StatisticsError:
        mode = "No unique mode"

    data_range = max(data) - min(data)  # Range
    variance = statistics.variance(data)  # Spread of data
    std_dev = statistics.stdev(data)  # Standard deviation

    # Return all results in a dictionary
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "range": data_range,
        "variance": variance,
        "standard_deviation": std_dev
    }

# Sample data
data = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

# Call function and print result
results = calculate_statistics(data)
print(results)
