import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

# enlace a base de datos vía sqlalchemy
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "estudiante.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# modelado
class Estudiante(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(20), nullable=True)
    apellido = db.Column(db.String(20), nullable=True)


    def __repr__(self):
        return "<Title: {}>".format(self.nombre)

# vistas
# @app.route("/")
@app.route("/", methods=["GET", "POST"])
def home():
    # return "My flask app"
    if request.form:
        print (request.form.get("title"))
        print(request.form)
        estudiante = Estudiante(nombre=request.form.get("title"), apellido = request.form.get("apellido"))
        db.session.add(estudiante)
        db.session.commit()
        return redirect("/")  

    
    estudiantes = Estudiante.query.all()
    return render_template("home.html", estudiantes=estudiantes)
    # return render_template("home.html")
    
@app.route("/update", methods=["POST"])
def update():
    nuevo_nombre = request.form.get("newtitle")
    nuevo_apellido = request.form.get("apellido")
    id_estudiante = request.form.get("idlibro")
    estudiante = Estudiante.query.get(id_estudiante)
    estudiante.nombre = nuevo_nombre
    estudiante.apellido = nuevo_apellido
    db.session.commit()
    return redirect("/")  

@app.route("/delete", methods=["POST"])
def delete():
    id_estudiante = request.form.get("idlibro")
    estudiante = Estudiante.query.get(id_estudiante)
    db.session.delete(estudiante)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



