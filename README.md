# Web Scraping Project

This project was completed as part of a freelancing task on Upwork. The goal was to scrape URLs from a website using Python and Selenium.

## Overview

The task involved scraping URLs from a specific webpage and saving them to a CSV file. The project utilized Python for scripting, Selenium for web scraping, and pandas for data manipulation.

## Technologies Used

### Python

Python was chosen as the primary programming language for its simplicity and extensive library support. It was used to write the web scraping script.

### Selenium

Selenium is a powerful tool for automating web browsers. It was used in this project to interact with the webpage, locate HTML elements, and extract URLs.

### Pandas

Pandas is a popular data manipulation library in Python. It was used to create a DataFrame from the extracted URLs and then save it to a CSV file.

## Files

### `scrape_urls.py`

This Python script contains the code for scraping URLs from the website. It utilizes the Selenium WebDriver to navigate the webpage, locate the relevant HTML elements, and extract the URLs. The extracted URLs are then stored in a CSV file.

### `urls.csv`

This CSV file contains the list of scraped URLs. Each URL is stored in a separate row under the header "URL".

## Getting Started

To run the web scraping script:

1. Install Python if you haven't already.
2. Install the required libraries: `pip install selenium pandas`.
3. Download the `scrape_urls.py` file.
4. Run the script using Python: `python scrape_urls.py`.
5. The scraped URLs will be saved to the `urls.csv` file.

## Note

- Ensure that you have the Chrome WebDriver installed and configured properly if using the Chrome browser with Selenium.
- Replace `'URL_OF_THE_WEBPAGE'` in the script with the actual URL of the webpage you want to scrape.

## License

This project is licensed under the [MIT License](LICENSE).

# upwork # selenium # pandas # scraper 
