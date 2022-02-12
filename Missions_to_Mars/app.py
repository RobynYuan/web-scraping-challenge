from flask import Flask, render_template, redirect
from matplotlib import collections
import scrape_mars
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_DB"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route('/')
def index():
	# Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
    # Return template and data
    return render_template('index.html',mars=mars)

@app.route('/scrape')
def scrape():

    #Run the Scrape function
   
    mars_data=scrape_mars.scrape_info()
   
    #update the mars database
    mars = mongo.db.mars
    mars.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)