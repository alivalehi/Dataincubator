import pandas as pd
import extractor as ex
titles = []
abstracts = []
authors_n = []
authors_a = []
date_ = [1802,1801,1712,1711,1710,1709,1708,1707,1706,1705,1704,1703,1702,1701]
max_n = 15000
len_max = 5
for d in date_:
	for i in range(400,max_n):
	    n_zer = len_max-len(str(i))
	    z= ''
	    for j in range(1,n_zer):
	        z = z+'0'
	    name = "https://arxiv.org/abs/"+str(d)+"."+z+str(i)
	    html_doc = ex.read_page(name)  
	    if "doesn't exist" in html_doc:
        	    break 
	    title = ex.extract_title(html_doc)
	    titles.append(title)
	    abstracts.append(ex.extract_abstract(html_doc))
	    address, names = ex.extract_authors(html_doc)
	    authors_n.append(names)
	    authors_a.append(address)
	    print(name)
	    if title is '':
	    	print(html_doc)
	se = pd.Series(titles)
	se2 = pd.Series(abstracts)
	se3 = pd.Series(authors_n)
	se4 = pd.Series(authors_a)    
	df = pd.DataFrame(columns=['title','abstracts','authors_n','authors_a'])
	df['title'] = se.values
	df['abstracts'] = se2.values
	df['authors_n'] = se3.values
	df['authors_a'] = se4.values
	df.to_csv('/home/ec2-user/Dataincubator/v1'+str(d)+'.csv')
