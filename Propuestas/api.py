from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hola123@127.0.0.1:5432/registro_sistemas'
db = SQLAlchemy(app)

class PruebaPersona(db.Model):
    __tablename__ = 'pruebaPersona'
    id_prueba = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    ethnic = db.Column(db.Text, nullable=False)
    sex = db.Column(db.Text, nullable=False)
    area = db.Column(db.Text, nullable=False)
    count = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    return 'Hola'
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://www.google.com/search?q=check+cookie+for+authentication++in+flask&rlz=1C1SQJL_enMX883MX883&sxsrf=ALiCzsZx-uov5I6lAfcGMDXhxYGaitn6lQ%3A1657758469210&ei=BWPPYtDADOyJkPIPnNeGqAU&ved=0ahUKEwiQ17jFj_f4AhXsBEQIHZyrAVUQ4dUDCA4&uact=5&oq=check+cookie+for+authentication++in+flask&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6CggAEOQCELADGAE6BAghEApKBAhBGABKBAhGGAFQlAJYxxpg7h5oAXAAeACAAYcBiAHZEJIBBDYuMTSYAQCgAQHIAQ3AAQHaAQYIARABGAk&sclient=gws-wiz#kpvalbx=_5KTPYqXWBuWgqtsPx52n-Ak17
@app.route('/user')
def get_user():
    row = PruebaPersona.query.filter_by(id_prueba=10).first()
    print("____________________________")
    print (row.ethnic)
    print("____________________________")

    return {"ethnic": row.ethnic}

