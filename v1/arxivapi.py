import urllib.request
url = 'http://export.arxiv.org/api/query?search_query=all:ali&start=0&max_results=100'
data = urllib.request.urlopen(url).read()
print(data)