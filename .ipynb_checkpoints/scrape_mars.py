
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

#Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
def scrape():

# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
@app '/scrape'

# Store the return value in Mongo as a Python dictionary.

#Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app '/'
index.HTML
# Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
