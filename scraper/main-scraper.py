import requests
from bs4 import BeautifulSoup
response = requests.get('file:///Users/alivalehi/Dropbox/project/Dataincubator/pdfminer.six/results/output.html')#../pdfminer.six/results/output.html')
html_doc = response.text
soup = BeautifulSoup(html_doc,'lxml')
body = soup.find('body')
pagefilling = ''.join(['%s' % x for x in soup.body.contents])
y = pagefilling.split("\n\n")
print(y[1])
