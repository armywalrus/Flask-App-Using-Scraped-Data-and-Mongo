# Dependencies
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser("chrome", **executable_path, headless=False)


    # NASA Mars News: Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    # Define URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # Print article headlines
    NASA_titles = soup.find_all('div', class_="content_title")
    title = NASA_titles[0].text
    # Print article paragraphs
    NASA_paragraphs = soup.find_all('div', class_="rollover_description_inner")
    paragraph = NASA_paragraphs[0].text


    #JPL Mars Space Images - Featured Image:
    # Define and open URL of page to be scraped
    splinter_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(splinter_url)
    # Scrape page into Soup
    splinter_html = browser.html
    splinter_soup = bs(splinter_html, "html.parser")
    # Print url of featured image
    for items in splinter_soup.select(".carousel_item"):
        featured_image_base_url = "https://www.jpl.nasa.gov"
        featured_image_url = featured_image_base_url + items['style'].split("url('")[1].split("')")[0]


    # Mars Facts table
    # Define URL of page to be scraped
    pandas_url = "https://space-facts.com/mars/"
    # Scrape the table containing facts about the planet including Diameter, Mass, etc.
    tables = pd.read_html(pandas_url)
    mars_column_one = (tables[0][0])
    mars_column_two = (tables[0][1])
    mars_facts = pd.DataFrame({"Attributes": mars_column_one,
                          " Mars Values": mars_column_two})
    mars_table = mars_facts.to_html(classes=['table_head', 'table_row', 'table_row_alternate', 'table_header'], index=False)


    # Obtain high resolution images for each of Mar's hemispheres.
    # Cerberus Hemisphere
    # Define and open URL of page to be scraped
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerberus_url)    
    # Scrape page into Soup
    cerberus_html = browser.html
    cerberus_soup = bs(cerberus_html, "html.parser")    
    # Print url of featured image
    cerberus_image_path = cerberus_soup.find_all('img')[5]["src"]
    cerberus_base_url = "https://astrogeology.usgs.gov"
    cerberus_image_url = cerberus_base_url + cerberus_image_path
    
    # Schiaparelli Hemisphere
    # Define and open URL of page to be scraped
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(schiaparelli_url)
    # Scrape page into Soup
    schiaparelli_html = browser.html
    schiaparelli_soup = bs(schiaparelli_html, "html.parser")
    # Print url of featured image
    schiaparelli_image_path = schiaparelli_soup.find_all('img')[5]["src"]
    schiaparelli_base_url = "https://astrogeology.usgs.gov"
    schiaparelli_image_url = schiaparelli_base_url + schiaparelli_image_path
    
    # Syrtis Hemisphere
    # Define and open URL of page to be scraped
    syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(syrtis_url)
    # Scrape page into Soup
    syrtis_html = browser.html
    syrtis_soup = bs(syrtis_html, "html.parser")    
    # Print url of featured image
    syrtis_image_path = syrtis_soup.find_all('img')[5]["src"]
    syrtis_base_url = "https://astrogeology.usgs.gov"
    syrtis_image_url = syrtis_base_url + syrtis_image_path
    
    # Valles Marineris Hemisphere
    # Define and open URL of page to be scraped
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_marineris_url)
    # Scrape page into Soup
    valles_marineris_html = browser.html
    valles_marineris_soup = bs(valles_marineris_html, "html.parser")
    # Print url of featured image
    valles_marineris_image_path = valles_marineris_soup.find_all('img')[5]["src"]
    valles_marineris_base_url = "https://astrogeology.usgs.gov"
    valles_marineris_image_url = valles_marineris_base_url + valles_marineris_image_path


    # Store data in a dictionary
    mars_news_dict = {"news_title": title,
            "news_paragraph":  paragraph,
            "featured_image": featured_image_url,
            "table": mars_table,
            "cerberus": cerberus_image_url,
            "schiaparelli": schiaparelli_image_url,
            "syrtis": syrtis_image_url,
            "valles_marineris": valles_marineris_image_url}

    # Close the browser after scraping
    browser.quit()

    return mars_news_dict    
