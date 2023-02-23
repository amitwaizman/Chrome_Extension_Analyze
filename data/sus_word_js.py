import os
import re

def sus(des):
    arr=[]
    allfiles2 = os.listdir(des)
    count=0
    count2=0
    for f in allfiles2:
        d=des + '/' +f
        extension = os.path.splitext(f)[1]
        if extension == ".js":
            count2+=1
            bol=True
            # Read in the JavaScript file
            with open(d, 'r') as f:
                try:   
                     javascript_code = f.read()
                except: 
                    bol=False
                # Define a regular expression to match URLs
                if bol:
        
                # Check if the JavaScript file contains document.write or innerHTML
                    if re.search(r'document\.write', javascript_code, re.IGNORECASE) or re.search(r'innerHTML', javascript_code, re.IGNORECASE):
                        count+=1
                #  else:
                #       print('False'
                bol=True    
    return count, count2   