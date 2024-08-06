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
