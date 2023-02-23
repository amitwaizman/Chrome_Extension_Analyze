import check_url as url
import from_css as c
import manifest as m
import os
import time
import numpy as np
import pandas as pd
import extract_url_js as e
import pre as p

des="/home/rivka/Desktop/chr/chromes/good_check"
#destination = '/home/seed/Desktop/chrom/try/3'

feature = ["permission" , "permission_number", "url_css", "check_css_for_script", "check_css_for_malicious_code", "js_check", 
           "js_url", "total_url", "premission_new", "label"]
feature_value = []
label = 0
feature_arrays = []
count_Js = 0
# gather all files
allfiles = os.listdir(des)
# allfiles = os.listdir(destination)
for i in range(2):
    allfiles = os.listdir(des)
    for f2 in allfiles:
        feature_value = [0 , 0 , 0 , 0, 0, 0 , 0, 0, 0, 0]
        d1=des + '/' +f2
        allfiles2 = os.listdir(d1)
        for f in allfiles2:
            d=d1 + '/' +f
            if "manifest.json" in d: 
                feature_value[0] =  m.permission(d)
                feature_value[1] =  m.permission_len(d)
                feature_value[8] =  p.help(d)
            elif ".css" in d:
                f1 = open(d , 'r')
                try:
                   f1.read()
                except:
                    break
                url_css= c.return_all_urls_in_css(f1.read())
                for u in url_css:
                    if url.is_urlopen(u) or url.is_regex_url(u) or url.Obfuscation(u):
                        feature_value[2] =  1        
                if c.check_css_for_script_like_code(f1.read()):
                        feature_value[3] =  1  
                if c.check_css_for_malicious_code(f1.read()):
                        feature_value[4] =  1
        print(d1)
        os.system("node js.js {} >> temp.txt".format(d1))
        temp = open("temp.txt", "r")
        js_check = temp.read()
        if 10 < int(js_check) < 20:
            feature_value[5] = 15
        elif 19 < int(js_check) < 30:
            feature_value[5] = 25
        elif 29 < int(js_check) < 40:
            feature_value[5] = 30
        elif 39 < int(js_check) < 50:
            feature_value[5] = 40
        elif 49 < int(js_check) < 60:
            feature_value[5] = 50
        elif 59 < int(js_check) < 70:
            feature_value[5] = 40
        elif 79 < int(js_check) < 89:
            feature_value[5] = 70
        else:
            feature_value[5] = 0
        os.system("rm temp.txt")
        # print(feature_value)  
        feature_value[6], feature_value[7] = e.count_susp_url(d1)
        feature_value[9] = label
        feature_arrays.append(feature_value)
    des="/home/rivka/Desktop/chr/chromes/mal_check"
    label = 1
arr = np.asarray(feature_arrays)
pd.DataFrame(arr).to_csv('sample8_test.csv', index=None) 