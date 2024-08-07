 # Highest-Grossing Japanese Films Scraper
## Description
This project scrapes data from Wikipedia's list of highest-grossing Japanese films and saves it to CSV files.

## Requirements
* #### Python 3.x
* #### requests library (install with 'pip install requests')
* #### beautifulsoup4 library (install with 'pip install beautifulsoup4')
* #### pandas library (install with 'pip install pandas')

## Installation

* #### Install the required libraries by running the following commands in your terminal:

```python
1. pip install requests
2. pip install beautifulsoup4
3. pip install pandas
4. pip install lxml
```
* #### Clone this repository or download the code.
* #### Run the script using Python (e.g., python scraper.py).

## Usage

1. #### The script will scrape data from the Wikipedia page and save it to CSV files in the same directory.
2. #### The CSV files will be named highest-grossing-japanese-films-table-number.csv, where number corresponds to the table number on the Wikipedia page.
## Notes
* #### Make sure you have the necessary permissions to write to the directory where the script is run.
* #### If you encounter any issues, check the script's output for error messages.
## Code
#### The code is written in Python and uses the requests, beautifulsoup4, and pandas libraries. The script is divided into the following steps:

1. #### Define the URL of the website to scrape
2. #### Send an HTTP GET request to the URL
3. #### Parse the HTML content using BeautifulSoup
4. #### Find all tables with the specified classes
5. #### Loop through each table and extract headers and rows
6. #### Convert the data to a DataFrame and save it to a CSV file

## Contributing

#### Contributions are welcome! Please submit a pull request with your changes and a brief description of what you've added or fixed.

## Acknowledgments
* #### Wikipedia for providing the data
* #### The requests, beautifulsoup4, and pandas libraries for making this project possible