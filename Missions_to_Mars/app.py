from flask import Flask, render_template, redirect
import scrape_mars
import pymongo
# Use PyMongo to establish Mongo connection
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_DB
collection= db.mars


# app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
# mongo = PyMongo(app)

# Create an instance of Flask
app = Flask(__name__)

# # Route to render index.html template using data from Mongo
@app.route('/')
def index():
	# Find one record of data from the mongo database
    mars = collection.find_one()
    # Return template and data
    return render_template('index.html',mars=mars)

@app.route('/scrape')
def scrape():

    #Run teh Scrape function

    scrape_mars.scrape_info()

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
