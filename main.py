import argparse
import json
import os
import re
from scraper import yield_iherb_nutrients

def save(json_obj, directory, category):
    prod_cd = json_obj.get('prod_cd', '')
    filepath = '{}/{}/iherb_{}.json'.format(directory, category, prod_cd)
    with open(filepath, 'w', encoding='utf-8-sig') as fp:
        json.dump(json_obj, fp, indent=2, ensure_ascii=False) 
    

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--directory', type=str,
                        default='./output_test',
                        help='Output directory')
    parser.add_argument('--sleep', type=float, default=1, help='Sleep time for each submission (post)')
    parser.add_argument('--verbose', dest='VERBOSE', action='store_true')
    
    args = parser.parse_args()
    directory = args.directory
    sleep = args.sleep
    VERBOSE = args.VERBOSE

    if not os.path.exists(directory):
            os.makedirs(directory)

    with open('categories.txt', 'r', encoding='utf-8-sig') as f:
            text = f.read()
            lines = text.split('\n')
            lines = filter(lambda x: x != '' and x is not None, lines)
            categories = sorted(set(lines))
            print(categories)

    for category in categories:
        os.makedirs(directory+'/{}'.format(category))
        print('Starts to scrap {} data...'.format(category))

        n_exceptions = 0
        for prod_data in yield_iherb_nutrients(category, sleep):
            try:
                save(prod_data, directory, category)
            except Exception as e:
                n_exceptions += 1
                continue
        if n_exceptions > 0:
            print('Exist %d nutrient exceptions' % n_exceptions)

if __name__ == '__main__':
    main()