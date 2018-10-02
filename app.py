# import modules and python file
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app. set up the app factory
app = Flask(__name__)

# Create connection variable to MongoDB
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
# inside of the pymongo toolbox i want to use the MongoClient tool on the project (path) mongodb://localhost:27017
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
# create a new DataBase in MongoDB
db = client.mars_db
collection = db.mars

@app.route("/")
def index():
    #find data set equal to mars var
    mars = mongo.db.mars.find_one()

    # go into template folder to get html doc
    return render_template("index.html", mars=mars)

# @app.route("/scrape")
# def scrape():
#     mars = 

# @app.route("/scrape")
# def scrape():
#     mars_data = scrape_mars.scrape()

#     mars = mongo.db.mars

#     mars.update({}, mars_data, upsert=True)

#     return redirect("http://localhost:5000/", code=302)

@app.route("/scrape")
def scrapper():
    mars_scrape = scrape.scrape()

    mongo.db.mars_scrape.update({}, mars_scrape, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)