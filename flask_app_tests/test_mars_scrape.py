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

    mars_hemisphere = [
    cerberus_img,
    schiaparelli_img,
    syrtis_img,
    valles_marineris_img
    ]

    mars_dict={"urls":mars_hemisphere}


    print(mars_dict)
    return mars_dict    


def cerebrusscrape():
    browser = init_browser()
    
    
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
    schiaparelli_img = schiaparelli_base_url + schiaparelli_image_path
    
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
    syrtis_img = syrtis_base_url + syrtis_image_path
    
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
    valles_marineris_img = valles_marineris_base_url + valles_marineris_image_path
    return valles_marineris_img    
    
   
    # Store data in a dictionary
    

