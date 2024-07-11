import time

def count_to_one_billion():
    c = 0
    for i in range(1, 1000000001):
        x = i*i
        c+=1
        pass  # No operation, just counting
    print(c)


start_time = time.time()
count_to_one_billion()
end_time = time.time()
print(f"Time taken to count to 1 billion: {end_time - start_time} seconds")
