from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_hemisphere = mongo.db.mars_hemisphere.find_one()
    return render_template("index.html", mars_hemisphere=mars_hemisphere)

@app.route("/scrape")
def scraper():
    mars_hemisphere = mongo.db.mars_hemisphere
    mars_hemisphere_datum = mars_scrape.scrape()
    mars_hemisphere.update({}, mars_hemisphere_datum, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)