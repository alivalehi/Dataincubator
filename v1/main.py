import extractor as ex
name = "https://arxiv.org/abs/1802.00254"#"https://arxiv.org/find/cs/1/au:+Wang_Y/0/1/0/all/0/1"#"https://arxiv.org/abs/1802.00254"
html_doc = ex.read_page(name)  
publications = ex.extract_list_of_author_publications(html_doc)
title = ex.extract_title(html_doc)
print(title)