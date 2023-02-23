import check_url as url
import os
import json 
import re
# extract the URL from JS and check if a suspicious


def count_susp_url(dir_crx):
   url_t = []
   allfiles2 = os.listdir(dir_crx)
   for f in allfiles2:
    d=dir_crx + '/' +f
    extension = os.path.splitext(f)[1]
    if extension == ".js":
            bol=True
            with open(d, 'r') as f:
                try:   
                 javascript_code = f.read()
                except: 
                 bol=False
                if bol:
                    url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
                    urls = re.findall(url_regex, javascript_code)
                    url_t.extend(urls)
                    url_t = list(set(url_t))
   count=0
   for u in url_t:
        if url.is_regex_url(u):
                count+=1
   bol=True       
   return count ,len(url_t)  