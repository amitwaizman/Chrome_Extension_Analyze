import requests
from bs4 import BeautifulSoup

def sus_html(file):
    count = 0
    response = requests.get(file)
    soup = BeautifulSoup(response.content, 'html.parser')
    suspicious_tags = soup.find_all(['script', 'iframe', 'meta', 'link'])
    if suspicious_tags:
        count+=1
    suspicious_scripts = soup.find_all('script', src=False)
    if suspicious_scripts:
        count+=1

    # Check the network traffic for suspicious connections
    for script in suspicious_scripts:
        if 'http' in script.text:
          count+=1
    return count
