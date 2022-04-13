from utils import get_soup
from dateutil.parser import parse
import re 

def parse_iherb(url): 
    
    # 1. 회사명 + 제품명
    def parse_title(soup):
        title = soup.find('div', class_ = 'product-summary-title').text.strip()
        if not title:
            return 'title error'
        return title 
    
    # 2. 제품코드
    def parse_prod_code(soup):
        prod_code = soup.find('span', itemprop = 'sku').text.strip()
        if not prod_code:
            return 'prod_code error'
        return prod_code
    
    # 3. 가격
    def parse_price(soup):
        try:
            price = soup.find('div', class_ = 'col-xs-15 col-md-15 price our-price').text.strip()
        except:
            price = soup.find('b', class_ = 's24').text.strip()
        price = re.sub('[\₩,]', '', price)
        if not price:
            return 'price error'
        return price
        
    # 4. 영양성분: {영양성분명: [함량, 기준치 충족%]}
    def parse_nutrients(soup):
        nutrients_dict = { tr.find_all('td')[0].text.strip():tr.find_all('td')[1].text.strip() for tr in tr_nutri_list}
        nutrients_dict = {re.sub(' ', '', i):re.sub('[\s,<*]', '', j) for i,j in nutrients_dict.items() if (j not in ['*', '**', '†'])}
        nutrients_dict = {re.search('([\w-]+)\(?', i).group(1): re.findall('([\d.]+)([\w]+)', j)[0] for i,j in nutrients_dict.items()}
        if not nutrients_dict:
            return 'nutrients_dict error' 
        return nutrients_dict
    
    # 5. 하루 섭취량
    def parse_serving(soup):

        serving = re.search('([0-9]+\s?)([a-zA-Z가-힣]+)', tr_info_list[1].text.strip().split(":")[1]).group(1).strip()
        unit = re.search('([0-9]+\s?)([a-zA-Z가-힣]+)', tr_info_list[1].text.strip().split(":")[1]).group(2).strip()
        
        if not serving or not unit:
            return "serving unit error"
        return [serving, unit]
    
    soup = get_soup(url)
    
    # 4,5에서 사용할 tr_list 선언
    tr_list = soup.find('div', class_ = 'supplement-facts-container').find_all('tr')
    tr_info_list = [tr for tr in tr_list if len(tr.find_all('td'))==1]
    tr_nutri_list = [tr for tr in tr_list[3:] \
                if (len(tr.find_all('td'))>=3) & (tr.find_all('td')[0].text.strip()!='') ]
    iherb_dic = {
        'url':  url,
        'title': parse_title(soup),
        'prod_cd': parse_prod_code(soup),
        'price': parse_price(soup),
        'nutrients': parse_nutrients(soup),
        'serving': parse_serving(soup)
        
    }
    return iherb_dic