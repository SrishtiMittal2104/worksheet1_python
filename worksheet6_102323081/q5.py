import time
import string
import random
import matplotlib.pyplot as plt

# Generate random text file of a specific size in MB
def generate_random_text(size_in_mb):
    size_in_bytes = size_in_mb * 1024 * 1024
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_bytes))

# Time the conversion to uppercase for different file sizes
sizes = [200, 400, 600, 800, 1000]
times = []

for size in sizes:
    text = generate_random_text(size)
    start_time = time.time()
    text_upper = text.upper()
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
    print(f"Time to convert {size} MB to uppercase: {elapsed_time:.2f} seconds")

# Plot the performance
plt.plot(sizes, times, marker='o')
plt.xlabel('File Size (MB)')
plt.ylabel('Time (seconds)')
plt.title('Time to Convert Files to Uppercase')
plt.grid(True)
plt.show()