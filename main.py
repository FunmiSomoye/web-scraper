from modules.db import connect_to_db, get_csv
from modules.scrape import scraper, write_to_csv
import pandas as pd

#input search word and numbere of search results
search_word = ''
no_of_results = 0

#input path to csv
path_to_csv = ''
table_name = ''

#set your database properties
user = ''
password = ''
host = ''
database = ''


def scrape_data(search_word:str, no_of_results:int) -> None:
    """
    This function scrapes the data and saves it to csv in your current path
    """

    entry = scraper(search_word, no_of_results)
    write_to_csv('bags', entry)


def send_to_db(user, password, host, database, path_to_csv, table_name):
    """
    This function imports csv data into heroku postgres database
    """

    db = connect_to_db(user, password, host, database)
    hello = get_csv(path_to_csv)
    hello.to_sql(table_name, db)

