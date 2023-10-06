from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Instantiate app.
app = Flask(__name__)

# Connect to database and initialize database object.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Chopin2718!@localhost/speedrun_timer'
db = SQLAlchemy(app)

# Database models.
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    
class Splits(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

class Runs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

class CategorySplits(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    split_id = db.Column(db.Integer, db.ForeignKey('splits.id'), nullable=False)
    split_order = db.Column(db.Integer, nullable=False)

class RunSplits(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run_id = db.Column(db.Integer, db.ForeignKey('runs.id'), nullable=False)
    split_id = db.Column(db.Integer, db.ForeignKey('splits.id'), nullable=False)
    split_hrs = db.Column(db.Integer, nullable=False)
    split_mins = db.Column(db.Integer, nullable=False)
    split_secs = db.Column(db.Integer, nullable=False)
    split_mss = db.Column(db.Integer, nullable=False)

# Create database tables.
# Requires an 'application context', whatever that means.
app.app_context().push()
db.create_all()



# Routes.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template("new.html")
    if request.method == 'POST':
        # Add created category to database
        return redirect('/')