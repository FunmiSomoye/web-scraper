import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = 'https://www.next.lt/en'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'referer': 'https://www.next.lt'
}


def scraper(search_word:str, size:int):
    """
    This funuction: 
    connects to www.next.lt/en, 
    scrapes data from it based on the search keyword and the number specified in 'size':
        - item category, item url, item image url and item price
    and returns a data frame
    """

    n = 0
    page_range = int(size/24 if size%24 == 0 else (size/24)+1)
    data = []
    for i in range(page_range):
        read_site = requests.get(f'https://www.next.lt/en/search?w={search_word}&srt{n}')
        soup = BeautifulSoup(read_site.content, 'html.parser') 

        product_list = soup.find_all('article', class_='Item')
        for item in product_list:
            the_title = (item.a['title']).split(' |')
            category = search_word.capitalize()
            title=the_title[0]
            price = the_title[1]
            data.append(
                {
                    'category': category,
                    'name': title,
                    'price': price,
                    'item_url': item.a['href'],
                    'image_url': item.img['src']
                })
            
            if len(data) >= size:
                break
        n+=24
        print(n)
    return pd.DataFrame(data)

def write_to_csv(filename: str, data: pd.DataFrame) -> None:
    """
    This function converts the data from a dataframe to a csv file
    """
    
    filename = filename + '.csv'
    data.to_csv(filename, index=False)





