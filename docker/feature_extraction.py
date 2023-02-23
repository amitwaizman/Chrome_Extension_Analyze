import manifest as manifest
import check_url as url
import from_css as c
import extract_url_js as e

import os
import time
import numpy as np
import pandas as pd


def feature(path):
    feature_value = [0 , 0 , 0 , 0, 0, 0 , 0, 0, 0]
    # gather all files
    allfiles = os.listdir(path)
    for f in allfiles:
            path_f = path + '/' + f
            if "manifest.json" in path_f: 
                    feature_value[0] =  manifest.permission(path_f)
                    feature_value[1] =  manifest.permission_len(path_f)
                    feature_value[8] =  manifest.permission_string(path_f)
            elif ".css" in path_f:
                    f1 = open(path_f , 'r')
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

            os.system("node check_js.js {} >> temp.txt".format(path))
            temp = open("temp.txt", "r")
            js_check = temp.read()
            try:
                int(js_check)
            except:
                js_check = 0
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
            feature_value[6], feature_value[7] = e.count_susp_url(path)

    print(feature_value)
    return feature_value    
