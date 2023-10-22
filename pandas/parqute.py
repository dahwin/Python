import pandas as pd

# Set the option to display all columns
pd.set_option('display.max_columns', None)

# Read the parquet file into a pandas DataFrame
df = pd.read_parquet(r"G:\download\train-00000-of-00206.parquet")

# Print the contents of the DataFrame
print(df['content'].head())
