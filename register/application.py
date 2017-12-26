from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Flask-SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///froshims3.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Registrant(db.Model):
	__tablename__ = 'registrants'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	dorm = db.Column(db.Text)

	def __init__(self, name, dorm):
		self.name = name
		self.dorm = dorm


@app.route("/")
def index():
	return render_template('templates/index.html')

@app.route("/register", methods=["POST"])
def register():
	if request.form["name"] == "" or request.form["dorm"] == "":
		return render_template("templates/failure.html")
	registrant = Registrant(request.form["name"], request.form["dorm"])
	db.session.add(registrant)
	db.session.commit()
	return render_template("success.html")

@app.route("/registrants")
def registrants():
	rows = Registrant.query.all()
	render_template("registrants.html", registrants=rows)

@app.route("/unregister", methods=["GET", "POST"])
def unregister():
	if request.method == "GET":
		# rows = db.execute("SELECT * FROM registrants")
		rows = Registrant.query.all()
		return render_template("unregister.html", registrants=rows)
	elif request.method == "POST":
		if request.form["id"]:
			# db.execute("DELETE FROM registrants WHERE id= :id", id=request.form["id"])
			Registrant.query.filter(Registrant.id == request.form["id"]).delete()
			db.session.commit()
		return redirect(url_for("registrants"))

