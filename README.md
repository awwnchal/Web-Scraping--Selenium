# Selenium: The Bored Ape Yacht Club

This repository contains code for web scraping and data analysis of two different websites using Selenium and regular web scraping techniques. The code is written in Python

# Overview
The first part of the project involves scraping the Bored Ape Yacht Club's OpenSea collection to obtain details of the most expensive apes with "Solid gold" fur. The details of the apes are then stored in HTML format on the local disk.

The second part of the project involves scraping information about the top 30 pizzerias in San Francisco from yellowpages.com. The information is then parsed and stored in a MongoDB collection. The addresses of the pizzerias are then geocoded using the Positionstack API and stored in the MongoDB collection.

# Requirements
The following packages are required to run the code:

Python 3.8 or higher,
Selenium WebDriver,
pymongo,
requests,
beautifulsoup4,


# Usage
To use the code, first clone the repository:

```ruby
git clone https://github.com/username/repository.git
```
Part 1: Bored Ape Yacht Club
1.Navigate to https://opensea.io/collection/boredapeyachtclub and select all apes with “Solid gold” fur and
sort them “Price high to low”.

2.Run the bored_ape_yacht_club.py file using the following command:

```ruby
python bored_ape_yacht_club.py <URL>
Replace <URL> with the URL obtained in step 1.
```
3.The details of the top 8 most expensive apes will be stored in HTML format on the local disk.

Part 2: San Francisco Pizzerias
1.Run the san_francisco_pizzerias.py file using the following command:

```ruby
python san_francisco_pizzerias.py
```
This will search for the top 30 "Pizzeria" in San Francisco on yellowpages.com and store the search result page in HTML format on the local disk.
2. Run the parse_pizzerias.py file using the following command:

```ruby
python parse_pizzerias.py
```
This will parse the search result page saved in step 1 and store the information about the top 30 pizzerias in a MongoDB collection called "sf_pizzerias".

Run the geocode_pizzerias.py file using the following command:
```ruby
python geocode_pizzerias.py
```
This will update the MongoDB collection "sf_pizzerias" with the geolocation (long, lat) of each pizzeria's address using the Positionstack API.

Conclusion
The code provided in this repository demonstrates the use of Selenium and regular web scraping techniques to obtain and analyze data from different websites. The code can be easily modified to scrape data from other websites and store the data in different formats.
