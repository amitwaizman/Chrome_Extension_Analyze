import os
import shutil
import json 

def open_file(path):
            if ".php" in path:
               return []
            file_name = open(path, mode='r', encoding='utf-8-sig')
            try:
             manifest = json.load(file_name)
            except:
             file_name = open(path, mode='r')
             manifest = json.load(path)
            return manifest.get('permissions', [])

 # Function that identifies malware by black list
def permission(path):
            permission_array = open_file(path)
            if len(permission_array) == 0:
                return 1
            malicious_permissions = ['experimental','accessibilityFeatures','FileSystem','Streaming','Clipboard']         
            for permission in malicious_permissions:
                if permission in permission_array:
                    return 1
            return 0
            

# Function that returns the amount of permissions
def permission_len(path):
            permission_array = open_file(path)
            return len(permission_array)
                  
      

def permission_string(path):
    str = ""
    str_permissions = set()  
    permission_array = open_file(path)
    temp =[]
    for i in permission_array:
        if i=='':
            temp.append('null')
        else:    
           temp.append(i) 
    for key in temp:
        str_permissions.add(key)
    for x in str_permissions:
          str+=  x +' '
    # print(a)
    if len(permission_array) == 0:
        return "null"
    return str 
