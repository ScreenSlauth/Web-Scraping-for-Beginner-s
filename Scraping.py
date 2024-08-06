import requests
from bs4 import BeautifulSoup
import pandas as pd
# Step 1: Define the URL of the website to scrape
url="https://en.wikipedia.org/wiki/List_of_highest-grossing_Japanese_films"
# Step 2: Send an HTTP GET request to the URL
response = requests.get(url)
print(response)
# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup = BeautifulSoup(response.text, "lxml")
print(soup)