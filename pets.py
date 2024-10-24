import os
from your_application import db  # Adjust the import based on your file structure

if os.path.exists('pets.db'):
    os.remove('pets.db')  # Remove the old database

with app.app_context():
    db.create_all()  # Create the database and tables with the new structure
