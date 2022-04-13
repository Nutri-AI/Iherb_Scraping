import json
import requests
import re
from dateutil.parser import parse
from utils import get_soup
from parser import parse_iherb

## caution: global times limit page 100, you should use date 

def yield_iherb_nutrients(category, sleep=1.0):
    
    ## get total product link 
    page = 1
    total_prod_list = []
    while True:
        try: 
            url = 'https://kr.iherb.com/c/{}?sr=2&noi=48&p={}'.format(category,page)
            soup = get_soup(url)
            sub_links = soup.find('div', class_='products').find_all('div', class_='absolute-link-wrapper')
            prod_links = [i.find('a')['href'] for i in sub_links]
            total_prod_list.extend(prod_links)
            page += 1
        except:
            break
    
    print('Total {} {} product links.'.format(len(total_prod_list), category))

    ## yield iherb nutrients data from each link
    for idx, url in enumerate(total_prod_list):
        try:
            json_obj = parse_iherb(url)
            print(url)
        except:
            print('failed to scrap data.')
            continue
        yield json_obj
        time.sleep(sleep)
        if idx%50 == 0:
            print('{}/{}'.format(idx, len(total_prod_list)), end=' ')

    print('Completed scraping {} data.\n'.format(category))