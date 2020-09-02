from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import new_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", image=mars_data)

@app.route("/scrape")
def scraper():
    mars_hemisphere = new_scrape.init_browser()
    mongo.db.collection.update({}, mars_hemisphere, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)