
# coding: utf-8

# In[ ]:

import requests
import pandas as pd
from bs4 import BeautifulSoup
import scholar as sc

def read_page(file_name):
    response = requests.get(file_name)#../pdfminer.six/results/output.html')
    html_doc = response.text
    return html_doc
def extract_subject(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    #class="leftcolumntitle mathjax"
    #article = soup.
 #   title = soup.find('div', class_='title mathjax') 
    subject= ''
    whole_box = soup.find_all('div', class_='leftcolumn')
    box = whole_box[0]
    div = box.find('div', class_='subheader')
    subject = div.find('h1').text
    if subject is '':
        print('empty subject')    
    return subject    
def extract_title(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    #class="leftcolumntitle mathjax"
    #article = soup.
 #   title = soup.find('div', class_='title mathjax') 
    title= ''
    whole_box = soup.find_all('div', class_='leftcolumn')
    for box in whole_box:
        title = box.find('h1', class_='title mathjax').text
    if title is '':
        print('empty title')    
    return title
def extract_abstract(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    #class="leftcolumntitle mathjax"
    #article = soup.
 #   title = soup.find('div', class_='title mathjax') 
 #   print(soup)
    abstract = ''
    whole_box = soup.find_all('div', class_='leftcolumn')
    for box in whole_box:
        query = box.find('blockquote', class_='abstract mathjax')
        unwanted = query.find('span')
        unwanted.extract()
        abstract = query.text.replace("\n", "")
    if abstract is '':
        print('empty abstract')    
    return abstract
def extract_authors(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    #class="leftcolumntitle mathjax"
    #article = soup.
 #   title = soup.find('div', class_='title mathjax') 
 #   print(soup)
    name=list()
    address=list()
    whole_box = soup.find_all('div', class_='authors')
    for box in whole_box:
        links = box.find_all('a')
        for link in links:
            address.append(link['href'])
            name.append(link.text)

    if not address:
       print('empty adress') 
    if not name:
       print('empty name')     
    return address,name
def extract_list_of_author_publications(html_doc):
    soup = BeautifulSoup(html_doc,'lxml')
    title = list()
    counter = 0
    name=list()
    address=list()
    whole_box = soup.find_all('div', id='dlpage')
    for box in whole_box:
        dls = box.find_all('dl')
        for dl in dls:
            dds = dl.find_all('dd')
            for dd in dds:
                query = dd.find('div', class_='list-title mathjax')
                unwanted = query.find('span')
                unwanted.extract()
                title.append(query.text.replace("\n", ""))
    return title
def extract_author_scholar_page(authors):
    # This method only works when we want to retrive 
    querier = sc.ScholarQuerier()
    query = sc.SearchScholarQuery()
    query.set_author(authors)
    querier.send_query(query)
    name = query.get_url()
    html_doc = read_page(name) 
    soup = BeautifulSoup(html_doc,'lxml')
    whole_box = soup.find_all('table')
    box = whole_box[0]    
    ali = box.find('tr')
    tds = ali.find_all('td')
    a = tds[1].find('a')
    link = a['href']
    return "https://scholar.google.com"+link
def extract_author_scholar_info(authors):
    # This method only works when we want to retrive 
    querier = sc.ScholarQuerier()
    query = sc.SearchScholarQuery()
    query.set_author(authors)
    querier.send_query(query)
    name = query.get_url()
    html_doc = read_page(name) 
    soup = BeautifulSoup(html_doc,'lxml')
    whole_box = soup.find_all('table')
    box = whole_box[0]    
    ali = box.find('tr')
    tds = ali.find_all('td')
    divs = tds[1].find_all('div')
    for div in divs:
        if "Verified email" in div:
            affil =  div.text.replace("Verified email at ", "")
        if "Cited" in div:
            cite =  div.text.replace("Cited by ", "")
            
            
    return affil

