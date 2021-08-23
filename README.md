# Web Scrapper
### [Next Lithuania][1]

This is a web scrapping project that scrapes from an ecommerce website - [Next Lithuania][1], and saves to a heroku postgres database.
This website sells different varieties of items. We will be access individual items by keyword and scrape the:

        - Name of item
        - Price
        - Image URL, and
        - Item URL

This project pushed to next-lt-scraper postgres database hosted on heroku.
You can create yours here: [Postgres db on Heroku][2]

The project contains the:
- `scrape.py` - For scrapping data and saving to csv file
- `db.py` - For writing data to db

However, you can easily run the codes in `main.py` that links all the codes in the modules folder in one place.


### Installation

```pip install bs4```
```pip install request```
```pip install pandas```
```pip install sqlalchemy```

### Usage
##### main.py

Empty string parameters have already been created for ease of use. 
You simply enter the parameters needed.

##### Parameters

###### input search word and number of search results
* search_word = " "
* no_of_results = 0

###### input path to csv and desired table name for your database on heroku
* path_to_csv = " " (the csv file containing your scraped data)
* table_name = " "

###### input your database credentials
* user = " "
* password = " "
* host = " "
* database = " "

###### actions 
The `scrape_data` function takes in 2 parameters:

        - search_word
        - no_of_results
    
It returns a csv file containing the scraped data to your current directory

The `send_to_db` function takes in all the other parameters:

        - search_word
        - no_of_results
    
It converts your csv file into a dataframe and writes a table with its contents into the postgres database on heroku


The maximum number of items on an etsy page is 24.


### Development
The project is currently completed but open to modifications

[1]: https://www.next.lt/en "Next Lithuania"
[2]: https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1 "Postgres db on Heroku"
