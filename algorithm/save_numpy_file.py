import numpy as np

# Create a large list of random numbers
large_array = np.random.randint(0, 1000, (1000000,))

# Save the list to a .npy file
np.save("large_array.npy", large_array)
