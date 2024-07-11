import time


if __name__ == "__main__":
    start_time = time.time()
    from speed_vanila import count_to_one_billion
    end_time = time.time()
    print(f"Time taken to count to 1 billion: {end_time - start_time} seconds")