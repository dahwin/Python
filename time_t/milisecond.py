import datetime

# Get the current datetime
now = datetime.datetime.now()

# Format the date and time, including milliseconds
date_stamp = now.strftime('%Y-%m-%d')
time_stamp = now.strftime('%H-%M-%S-%f')[:-3]  # Truncate to milliseconds

# Construct the final timestamp string
time_stamp = f"""
date: {date_stamp}
time: {time_stamp}
"""

# Print the timestamp
print(time_stamp)
