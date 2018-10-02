# import modules
import time
import regex as re
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs

# set up scrape function to pull mars data from various websites
def scrape__():
  
    # set path for chrome broswer to open a blank chrome page
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = True)

    # set up empty dicts to append
    mars_data = {}

# .___  ___.      ___      .______          _______.   .__   __.  ___________    __    ____   _______.
# |   \/   |     /   \     |   _  \        /       |   |  \ |  | |   ____\   \  /  \  /   /  /       |
# |  \  /  |    /  ^  \    |  |_)  |      |   (----`   |   \|  | |  |__   \   \/    \/   /  |   (----`
# |  |\/|  |   /  /_\  \   |      /        \   \       |  . `  | |   __|   \            /    \   \    
# |  |  |  |  /  _____  \  |  |\  \----.----)   |      |  |\   | |  |____   \    /\    / .----)   |   
# |__|  |__| /__/     \__\ | _| `._____|_______/       |__| \__| |_______|   \__/  \__/  |_______/    
# 

    # use splinter and browser to connect to nasa website 
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)
    time.sleep(2)

    # read the html 
    html = browser.html
    soup = bs(html, 'html.parser')

    # search the most recent post for title and text
    news_title = soup.find("div", class_ = "content_title").text
    news_paragraph = soup.find("div", class_ = "article_teaser_body").text

    # add this data to mars_data dict
    mars_data["news_title"] = news_title
    mars_data["news_paragraph"] = news_paragraph

# .___  .__.      ___      .______          _______.    __  .___  ___.      ___       _______  _______ 
# |   \/   |     /   \     |   _  \        /       |   |  | |   \/   |     /   \     /  _____||   ____|
# |  \  /  |    /  ^  \    |  |_)  |      |   (----`   |  | |  \  /  |    /  ^  \   |  |  __  |  |__   
# |  |\/|  |   /  /_\  \   |      /        \   \       |  | |  |\/|  |   /  /_\  \  |  | |_ | |   __|  
# |  |  |  |  /  _____  \  |  |\  \----.----)   |      |  | |  |  |  |  /  _____  \ |  |__| | |  |____ 
# |__|  |__| /__/     \__\ | _| `._____|_______/       |__| |__|  |__| /__/     \__\ \______| |_______|
                                                                                                    
    # connects to jpl.nasa url
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    time.sleep(2)

    # clicks on the full image button
    browser.find_by_id('full_image').first.click()

    # opens all of the the html for the page as a big block, non prettify-able
    image_html = browser.html

    # reads through the html on the page, is prettify-able
    soup = bs(image_html, "html.parser")

    # find the specific tag and class for the image I am looking for
    # featured_image_url = image_url + soup.find("img", class_="fancybox-image")["src"]
    featured_image_url = image_url + soup.find("a", class_="fancybox")["data-fancybox-href"]

    # add this data to mars_data dict
    mars_data["featured_image_url"] = featured_image_url


# .___  ___.      ___      .______          _______.   ____    __    ____  _______     ___   .___________. __    __   _______ .______      
# |   \/   |     /   \     |   _  \        /       |   \   \  /  \  /   / |   ____|   /   \  |           ||  |  |  | |   ____||   _  \     
# |  \  /  |    /  ^  \    |  |_)  |      |   (----`    \   \/    \/   /  |  |__     /  ^  \ `---|  |----`|  |__|  | |  |__   |  |_)  |    
# |  |\/|  |   /  /_\  \   |      /        \   \         \            /   |   __|   /  /_\  \    |  |     |   __   | |   __|  |      /     
# |  |  |  |  /  _____  \  |  |\  \----.----)   |         \    /\    /    |  |____ /  _____  \   |  |     |  |  |  | |  |____ |  |\  \----.
# |__|  |__| /__/     \__\ | _| `._____|_______/           \__/  \__/     |_______/__/     \__\  |__|     |__|  |__| |_______|| _| `._____|
                                                                                                                                         

    # set path to mars weather report Twitter page
    weather_url = "https://twitter.com/MarsWxReport?lang=en"
    browser.visit(weather_url)
    time.sleep(2)

    # read the html
    html = browser.html
    soup = bs(html, 'html.parser')

    # find the paragraph tab, 
    mars_soup = soup.find_all("p", class_="TweetTextSize")

    weather_list = []

    for weather in mars_soup:
        
        if re.search("Sol ", weather.text):
            weather_list.append(weather.text)

    # pull just the first weather report from the list       
    mars_weather = weather_list[0]
    # add this data to mars_data dict
    mars_data["mars_weather"] = mars_weather


# .___  ___.      ___      .______          _______.    _______    ___       ______ .___________.    _______.
# |   \/   |     /   \     |   _  \        /       |   |   ____|  /   \     /      ||           |   /       |
# |  \  /  |    /  ^  \    |  |_)  |      |   (----`   |  |__    /  ^  \   |  ,----'`---|  |----`  |   (----`
# |  |\/|  |   /  /_\  \   |      /        \   \       |   __|  /  /_\  \  |  |         |  |        \   \    
# |  |  |  |  /  _____  \  |  |\  \----.----)   |      |  |    /  _____  \ |  `----.    |  |    .----)   |   
# |__|  |__| /__/     \__\ | _| `._____|_______/       |__|   /__/     \__\ \______|    |__|    |_______/    
                                                                                                           
    # set path to website
    url = "https://space-facts.com/mars/"
    time.sleep(2)

    # read the table at the url destination
    tables = pd.read_html(url)
    tables[0]

    # set up dataframe
    df = tables[0]
    df.columns = ["Categories", "Measurements"]
    df.set_index(["Categories"])

    # convert html to df
    html_table = df.to_html()
    #replace all the \n with an empty space instead
    html_table.replace('\n', '')

    # save table as html
    # df.to_html("table.html")
    mars_data["html.table"] = "html_table"


#  __    __   _______ .___  ___.  __       _______..______    __    __   _______ .______       _______     _______.
# |  |  |  | |   ____||   \/   | |  |     /       ||   _  \  |  |  |  | |   ____||   _  \     |   ____|   /       |
# |  |__|  | |  |__   |  \  /  | |  |    |   (----`|  |_)  | |  |__|  | |  |__   |  |_)  |    |  |__     |   (----`
# |   __   | |   __|  |  |\/|  | |  |     \   \    |   ___/  |   __   | |   __|  |      /     |   __|     \   \    
# |  |  |  | |  |____ |  |  |  | |  | .----)   |   |  |      |  |  |  | |  |____ |  |\  \----.|  |____.----)   |   
# |__|  |__| |_______||__|  |__| |__| |_______/    | _|      |__|  |__| |_______|| _| `._____||_______|_______/    
    
    # set up an empty list to append {title, img_url} dicts to
    hemispheres_list = []

    # VALLES MARINERIS
    # set up chrome driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # set up connection to url and click on link
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")

    # use BeautifulSoup to parse html data
    html = browser.html
    soup = bs(html, "html.parser")

    # set up link to html path
    valles_link = soup.find('div', 'downloads').a['href']

    # set up dictionary with title and img_url
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # append dict to hemispheres list
    hemispheres_list.append(valles_marineris)

    # CERBERUS HEMISPHERE
    # set up chrome driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # set up connection to url and click on link
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")

    # use BeautifulSoup to parse html data
    html = browser.html
    soup = bs(html, "html.parser")

    # set up link to html path
    cerberus_link = soup.find('div', 'downloads').a['href']

    # set up dictionary with title and img_url
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # append dict to hemispheres list
    hemispheres_list.append(cerberus)

    #SCHIAPARELLI HEMISPHERE
    # set up chrome driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # set up connection to url and click on link
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")

    # use BeautifulSoup to parse html data
    html = browser.html
    soup = bs(html, "html.parser")

    # set up link to html path
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # set up dictionary with title and img_url
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": cerberus_link
    }

    # append dict to hemispheres list
    hemispheres_list.append(schiaparelli)

    # SYRTIS MAJOR HEMISPHERE
    # set up chrome driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # set up connection to url and click on link
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")

    # use BeautifulSoup to parse html data
    html = browser.html
    soup = bs(html, "html.parser")

    # set up link to html path 
    syrtis_link = soup.find('div', 'downloads').a['href']

    # set up dictionary with title and img_url
    syrtis = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # append dict to hemispheres list
    hemispheres_list.append(syrtis)

    mars_data["hemispheres_list"] = hemispheres_list

    return mars_data
    # print(mars_data)
scrape__()