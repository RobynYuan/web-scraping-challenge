import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_DB
collection= db.mars
def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Visit redplantscience.com
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(1)

    # Scrape page into Soup
  
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    # Get the news title and news paragraph
    news_title=soup.find_all('div', class_='content_title')[0].text
    news_paragraph=soup.find_all('div',class_='article_teaser_body')[0].text


    # Find the src for the image from spaceimages-mars.com


    image_url ='https://spaceimages-mars.com/'

    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image=soup.find_all('a', class_='showimg fancybox-thumbs')
    featured_image_url=image_url+image[0].get('href')
   
    #find the table data comparing mars and earth


    mars_table_url ='https://space-facts.com/mars/'

    mars_table = pd.read_html(mars_table_url)
    mars_table=mars_table[0]

    earth_table_url='https://space-facts.com/earth/'
    earth_table = pd.read_html(earth_table_url)
    earth_table=earth_table[0]

    joined_table=pd.merge(mars_table, earth_table, how='inner', on=0)
    joined_table.columns = ['Description', 'Mars','Earth']
    joined_table.set_index('Description')
    html_table= joined_table.to_html()
    
    #scarpe the image URL and the image titile from https://marshemispheres.com/ 

    image_url_1='https://marshemispheres.com/'
    browser.visit(image_url_1)
    html = browser.html

    soup = BeautifulSoup(html,'html.parser')
    images=soup.find_all('img', class_='thumb')
    titles=soup.find_all('h3')
    img_urls=[]
    title_list=[]
    for i in range(4):
        image_url=image_url_1+images[i].get('src')
        img_urls.append(image_url)
        title_list.append(titles[i].get_text())


    hemisphere_image= {
             "title": title_list,
            "img_url": img_urls
                }
    hemisphere_image

    # Store all the scraped data in a dictionary mars_data
    mars_data = {
       "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image_url,
        "table":html_table,
        "hemispheres_image_url":img_urls,
        "hemispheres_image_title":title_list

    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    print(mars_data)
    collection.insert_one(mars_data)
    return mars_data
