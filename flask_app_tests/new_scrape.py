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
        print(featured_image_url) 



    mars_news_dict={"newstitle": title,
            "newsparagraph":  paragraph,
            "featured_image": featured_image_url}


    print(mars_news_dict)


    return mars_news_dict    

    
