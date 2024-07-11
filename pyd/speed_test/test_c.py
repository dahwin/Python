import time
import cython_ex

start_time = time.time()
cython_ex.count_to_ten_billion()
end_time = time.time()
print(f"Time taken to count to 1 billion: {end_time - start_time} seconds")
