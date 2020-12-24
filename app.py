import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_films")
def get_films():
    films = list(mongo.db.films.find())
    return render_template("films.html", films=films)


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        film = {
            "film_name": request.form.get("film_name"),
            "film_description": request.form.get("film_description"),
            "genre_name": request.form.get("genre_name"),
            "release_date": request.form.get("release_date"),
            "age_restriction": request.form.get("age_restriction"),
            "actor_name": request.form.get("actor_name"),
            "director_name": request.form.get("director_name"),
            "secret_pin": "1234",
        }
        mongo.db.films.insert_one(film)
        flash("New Film Added Succesfully")
        return redirect(url_for("get_films"))
        
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_film.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
