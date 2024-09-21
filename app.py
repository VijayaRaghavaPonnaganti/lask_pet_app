from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Pet {self.name}>'

# Route to display all pets
@app.route('/')
def index():
    pets = Pet.query.all()  # Get all pets from the database
    return render_template('index.html', pets=pets)

# Route to add a new pet
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        species = request.form['species']

        # Create a new Pet instance and add it to the database
        new_pet = Pet(name=name, species=species)
        db.session.add(new_pet)
        db.session.commit()  # Commit the changes
        return redirect(url_for('index'))  # Redirect to the pet list

    return render_template('add_pet.html')  # Render the add pet form

# Route to delete a pet
@app.route('/delete/<int:pet_id>')
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)  # Get the pet or return a 404 error
    db.session.delete(pet)  # Delete the pet from the session
    db.session.commit()  # Commit the changes
    return redirect(url_for('index'))  # Redirect to the pet list

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database and tables if they don't exist
    app.run(debug=True)  # Run the application in debug mode
