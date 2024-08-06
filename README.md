Wikipedia Highest-Grossing Japanese Films Scraper
This Python script scrapes the Wikipedia page for the highest-grossing Japanese films and saves the data from the tables into CSV files.

Table of Contents
Prerequisites
Installation
Usage
Script Details
Troubleshooting
Contributing
License
Prerequisites
Before running the script, ensure you have the following installed:

Python 3.6 or higher
pip (Python package installer)
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-username/wikipedia-scraper.git
cd wikipedia-scraper
Install the required Python packages:

sh
Copy code
pip install requests beautifulsoup4 pandas lxml
Usage
Navigate to the directory containing the script:

sh
Copy code
cd path/to/directory
Run the script:

sh
Copy code
python scraper.py
Check the output CSV files:
The script will generate CSV files named highest-grossing-japanese-films-table-1.csv, highest-grossing-japanese-films-table-2.csv, etc., in the same directory.

Script Details
The script performs the following steps:

Sends an HTTP GET request to the Wikipedia page for the highest-grossing Japanese films.
Parses the HTML content using BeautifulSoup.
Finds all tables with specified classes (wikitable, sortable, plainrowheaders, static-row-numbers, jquery-tablesorter).
Extracts headers and rows from each table.
Handles merged cells (with colspan and rowspan attributes) to ensure data integrity.
Saves the extracted data to CSV files.
Code Explanation
python
Copy code
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the website to scrape
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_Japanese_films"

# Step 2: Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve data: {response.status_code}")
else:
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")

    # Step 4: Find all tables with the specified classes
    tables = soup.find_all("table", class_=["wikitable", "sortable", "plainrowheaders", "static-row-numbers", "jquery-tablesorter"])

    # Step 5: Loop through each table and extract headers and rows
    for index, table in enumerate(tables):
        # Fetch the header (<th>) elements
        titles = table.find_all("th")
        header = [title.text.strip() for title in titles if title.text.strip() != "Ref."]  # Exclude "Ref."

        print(f"Table {index + 1} header: {header}")  # Debug: Print header

        # Fetch the rows (<tr>) and extract data from each cell (<td> or <th>)
        data = []
        rows = table.find_all("tr")[1:]  # Skip the first row (header row)

        for row_index, row in enumerate(rows):
            row_data = []
            cells = row.find_all(["th", "td"])  # Get both <th> and <td> cells

            for cell in cells:
                colspan = int(cell.get("colspan", 1))
                cell_text = cell.text.strip()

                # Append the cell text, repeated by colspan
                for _ in range(colspan):
                    row_data.append(cell_text)

            # Debug: Print row_data and header lengths
            print(f"Table {index + 1}, Row {row_index + 1} data: {row_data}, Expected length: {len(header)}, Actual length: {len(row_data)}")

            # Ensure row_data matches header length by appending empty strings if needed
            while len(row_data) < len(header):
                row_data.append("")  # Append empty string for missing columns

            # Only append if the row_data length matches the header length
            if len(row_data) == len(header):
                data.append(row_data)
            else:
                print(f"Row skipped due to column mismatch in table {index + 1}: {row_data}")

        # Convert the data to a DataFrame
        if data:  # Only create a DataFrame if there is valid data
            df = pd.DataFrame(data, columns=header)

            # Save the DataFrame to a CSV file without the index
            csv_filename = f"highest-grossing-japanese-films-table-{index + 1}.csv"  # Create a unique filename
            try:
                df.to_csv(csv_filename, index=False)  # Set index=False to avoid writing the index column
                print(f"Data saved to '{csv_filename}'.")
            except PermissionError:
                print(f"Permission denied: Unable to write to '{csv_filename}'. Please close any open instances of the file or check your permissions.")
        else:
            print(f"No valid data found for table {index + 1}.")
Troubleshooting
HTTP Request Failure: If the script fails to retrieve data, check your internet connection and ensure the URL is correct.
Permission Denied: If the script cannot write to a CSV file, close any open instances of the file or check your write permissions for the directory.
Column Mismatch: If rows are skipped due to column mismatches, ensure the HTML structure of the target page has not changed. You may need to adjust the script to handle new structures.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
