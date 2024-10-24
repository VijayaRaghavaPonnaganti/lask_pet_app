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
    ('Raja', 'Indian Pariah Dog', 3, 'Amit Sharma', 'Loyal and protective.'),
    ('Rani', 'Rajapalayam', 2, 'Anjali Mehta', 'Calm and friendly.'),
    ('Sheru', 'Gaddi Dog', 5, 'Rajesh Kumar', 'Brave and intelligent.'),
    ('Tuffy', 'Kanni', 4, 'Sita Iyer', 'Fast and agile.'),
    ('Bholu', 'Chippiparai', 3, 'Priya Singh', 'Energetic and alert.'),
]

# Execute insert statements
cursor.executemany('''
INSERT INTO pets (name, species, age, owner, description)
VALUES (?, ?, ?, ?, ?)
''', pets_to_insert)
cursor.execute('SELECT * FROM pets')

# Fetch all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()

