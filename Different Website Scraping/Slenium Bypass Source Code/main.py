
from time import sleep
import requests
from selenium import webdriver
import undetected_chromedriver as uc

if __name__ == '__main__':
    driver = uc.Chrome()
    # the targeted website you want to scrape
    driver.get('https://sau.ac.bd/')
    driver.maximize_window()
    sleep(10)

    html_doc = driver.page_source
    file = open("content.html", "w", encoding="utf-8")
    # rename the file like when you scraping homepage so, homepage.html
    # Or, when you scraping subpaage just edit that subapge.html
    # So, it's can help you understand the difference between the file
    file.write(html_doc)
    file.close()

    driver.close();







