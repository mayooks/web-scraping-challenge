# Automates browser actions
from splinter import Browser

# Parses the HTML
from bs4 import BeautifulSoup
import pandas as pd
import time
# For scraping with Chrome
from webdriver_manager.chrome import ChromeDriverManager
from flask import jsonify


def scrape():
    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Set an empty dict for listings that we can save to Mongo
    # listings = {"planet_images":img_urls}

    # The url we want to scrape
    url = "https://marshemispheres.com/"

    # Call visit on our browser and pass in the URL we want to scrape
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html

    ######################################################################

    # grabbing all links to the images on homepage
    links = browser.find_by_css("a.product-item img")

    img_urls = []

    # finding the the title and link of every image
    for i in range(len(links)):
        marshemispheres = {}

        browser.find_by_css("a.product-item img")[i].click()
        # link.click()
        time.sleep(1)
        # appending the scrapped data to the results dictionary
        element = browser.links.find_by_text("Original").first
        marshemispheres["title"] = browser.find_by_css("h2.title").text
        marshemispheres["img_url"] = element["href"]

        # appening the results dictionary into the img_urls list
        img_urls.append(marshemispheres)
        browser.back()
        time.sleep(1)
    # close the browser
    # browser.quit()
    print(img_urls)


    # Quit the browser
    # browser.quit()

    ######################################################################
    ######################################################################
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_link = url + soup.find('img', class_="headerimage")["src"]


    ######################################################################
    ######################################################################
    url = "https://galaxyfacts-mars.com/"

    mars_facts_df = pd.read_html(url)[1]

    mars_facts_df.columns = ["Description", "Mars"]
    mars_facts_df.set_index("Description", inplace=True)

    #### removing unwanted newlines to clean up the table.
    #mars_planet_profile_html.replace('\n', '')

    # show table


    # listings["mars_table"] = mars_planet_profile_html
    ######################################################################
    ######################################################################

    # browser.quit()
    ######################################################################
    ######################################################################

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    headlines = []

    # scrapping the data
    for x in range(0, 15):
        time.sleep(1)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        redplanet = {}

        titles = soup.findAll(name='div', attrs="content_title")
        # for title in titles:
        # print(title.text)

        redplanet['titles'] = browser.find_by_css("div.content_title")[x].text
        redplanet['teaser'] = browser.find_by_css("div.article_teaser_body")[x].text

        headlines.append(redplanet)

        # for headline, teaser_text in zip (headline_titles, teaser_paragraph):
        # results['titles'] = headline.text
        # results['teaser'] = teaser_text.text

        # headlines.append(results)
        # time.sleep(2)

        # browser.quit()

        ######################################################################
    listings = {"planet_images": img_urls,
                "featured_image": featured_image_link,
                "mars_table": mars_facts_df.to_html(classes="table table-striped"),
                "latest_news": headlines
                }

        # Return our dictionary
    return listings
