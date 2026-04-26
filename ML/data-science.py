import statistics
import numpy as np
import math
data = [10,20,30,40,50]
print("Square root of 25: ",math.sqrt(25))
print("Mean: ", statistics.mean(data))
print("Median: ",statistics.median(data))
print("Mode: ",statistics.median(data))
array = np.array(data)
print("Numpy array: ", array)
print("Sum using numpy: ",np.sum(data))
print("Standard deviation using numpy: ",np.std(data))
