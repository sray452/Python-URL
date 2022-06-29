'''
Program Name: Program 12_4.py
Prgram Description: This program uses the class stock to create objects with stock attributes.
Programmer: Ray, Stephen
Date: 03/27/2022
Course: CSC233-1L1
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def main():
    

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    counter = 0
    tags = soup('p')
    for tag in tags:

        counter = counter + 1

        #print(tag.get('href', None))

    print(counter)

    

main()
