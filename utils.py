import json
import re 
import requests
from bs4 import BeautifulSoup
from time import sleep

def get_soup(url, headers=None):
    """
    Arguments
    ---------
    url : str
        Web page url
    headers : dict
        Headers for requests. If None, use Mozilla/5.0 as default user-agent
    Returns
    -------
    soup : bs4.BeautifulSoup
        Soup format web page
    """

    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    html = r.text
    page = BeautifulSoup(html, 'lxml')
    return page
