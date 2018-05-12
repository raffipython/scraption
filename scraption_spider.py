# -*- coding: utf-8 -*-
"""
Scraption v1.0

"""

import argparse
import datetime
import csv


import os
import sys
import re
import requests

def blacklist_reader(filename):
    """Reads a config file and returns a list of blacklist websites"""
    blacklist = []
    with open(filename, 'r') as fd:
        f = fd.read()
        for line in f.split("\n"):
            if line:
                blacklist.append(line.replace(' ', ''))
    return blacklist
    
def csv_writer(URL, url_list):
    """Writes a list of URLs to a local file named url_list_<URL>_<TODAY'S DATE>.csv
       FORMAT:
           "Main URL", "# of URLs found", "List of URLs found"
           www.google.com, 4, www.g.com www.oo.com www.g.com www.le.com
    """
    
    TODAY = datetime.date.today() 
    URL_FILENAME = URL.split("//")[1].replace('.', '_')
    with open("URL_list_{}_{}.csv".format(URL_FILENAME, TODAY), 'w') as csvfile:
        urlwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        urlwriter.writerows(["Main URL", "# of URLs found", "List of URLs found"])
        urlwriter.writerows(url_list)




def url_crawler(URL):
    resp = requests.get(URL)
    print(resp)








def main(URL, BLACKLIST, DEPTH):
    
    
    
    
    
    
    print(URL, BLACKLIST, DEPTH)
    
    
    
    
    url_list = URL.split() 
    
    csv_writer(URL, url_list)
    
    url_crawler(URL)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scraption WebCrawler')
    parser.add_argument('-u','--url', help='URL to be scraped', required=True)
    parser.add_argument('-b','--blacklist', help='URLs not to scrape', required=True)
    parser.add_argument('-d','--depth', type=int, help='Depth/Frequency', required=True)
    args = parser.parse_args()
        
    URL = args.url
    BLACKLIST = blacklist_reader(args.blacklist)
    DEPTH = args.depth
        
    main(URL, BLACKLIST, DEPTH)





