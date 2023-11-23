import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:\\Users\\ALL USER\\Desktop\\Python\\sql\\alchemy\\dahwin.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to fetch all data from the 'people' table
cursor.execute('SELECT * FROM people')

# Fetch all the records as a list of tuples
data = cursor.fetchall()

# Close the cursor and the database connection
cursor.close()
conn.close()

# Print the fetched data
for row in data:
    print(row)
