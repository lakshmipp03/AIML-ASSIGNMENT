import numpy as np
import time

# Create 1 million numbers
size = 1000000

# Python List
python_list = list(range(size))

start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()

python_time = end - start

# NumPy Array
numpy_array = np.arange(size)

start = time.time()
numpy_result = numpy_array * 2
end = time.time()

numpy_time = end - start

print("Python List Time:", python_time)
print("NumPy Array Time:", numpy_time)