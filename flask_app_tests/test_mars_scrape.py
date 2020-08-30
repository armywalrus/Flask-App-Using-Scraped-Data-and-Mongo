# Dependencies
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

# Scrape.py test: high-res images
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_hemisphere = {}
    
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
    cerberus_img = cerberus_base_url + cerberus_image_path
    
    # Store data in a dictionary
    cerebrus_dict = {
    "Cerberus" : cerberus_img}
    
    # Append dictionary into list:
    mars_hemispheres_list = []
    mars_hemispheres_list.append(dict(cerebrus_dict))
    mars_hemisphere["Cerberus"] = mars_hemispheres_list

    return mars_hemisphere