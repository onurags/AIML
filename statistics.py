# ----------------------------------------
# 1. Using Python's statistics module
# ----------------------------------------
import statistics

data = [1, 2, 3, 4, 5, 5]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

print("== Python statistics module ==")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {stdev}\n")


# ----------------------------------------
# 2. Using NumPy for numerical operations
# ----------------------------------------
import numpy as np

array = np.array([1, 2, 3, 4, 5])
mean_np = np.mean(array)
std_np = np.std(array)
sum_np = np.sum(array)

print("== NumPy module ==")
print(f"Mean: {mean_np}")
print(f"Standard Deviation: {std_np}")
print(f"Sum: {sum_np}\n")


# ----------------------------------------
# 3. Using math module for basic math
# ----------------------------------------
import math

sqrt_val = math.sqrt(25)
power_val = math.pow(2, 3)
log_val = math.log(10)

print("== Math module ==")
print(f"Square Root of 25: {sqrt_val}")
print(f"2 raised to the power 3: {power_val}")
print(f"Natural log of 10: {log_val}\n")


# ----------------------------------------
# 4. Using SciPy for statistics
# ----------------------------------------
from scipy import stats

data_sp = [1, 2, 3, 4, 5]
mean_sp = stats.tmean(data_sp)
median_sp = np.median(data_sp)
mode_sp = stats.mode(data_sp, keepdims=True)  # keepdims avoids future warning
stdev_sp = stats.tstd(data_sp)

print("== SciPy stats module ==")
print(f"Mean: {mean_sp}")
print(f"Median: {median_sp}")
print(f"Mode: {mode_sp.mode[0]} (Count: {mode_sp.count[0]})")
print(f"Standard Deviation: {stdev_sp}")
