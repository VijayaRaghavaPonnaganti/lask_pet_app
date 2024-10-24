import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('pets.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for pets
cursor.execute('''
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER,
    owner TEXT,
    description TEXT
)
''')
pets_to_insert = [
    ('Buddy', 'Dog', 3, 'John Doe', 'Friendly and playful.'),
    ('Whiskers', 'Cat', 2, 'Jane Smith', 'Loves to nap in the sun.'),
    ('Goldie', 'Fish', 1, 'Tom Brown', 'Bright and energetic.'),
]

# Execute insert statements
cursor.executemany('''
INSERT INTO pets (name, species, age, owner, description)
VALUES (?, ?, ?, ?, ?)
''', pets_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Pets table created successfully!")
