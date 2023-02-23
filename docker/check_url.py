import urllib
import urllib.request
import re
import obfuscation_detection as od

def is_url_malicious(url):
    try:
        urllib.request.urlopen(url)
        return False  # URL is not malicious
    except urllib.error.URLError:
        return True  # URL is malicious


def is_regex_url(url):
    regex = "^((http|https)://)[-a-zA-Z0-9@:%.\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%.\\+~#?&//=]*)$"
    r = re.compile(regex)

    if (re.search(r, url)):
        return False
    else:
        return True

def is_malicious(url):
    regex = r"(?:https?|ftp)://[^\s/$.?#].[^\s]\.[^\s]"
    if re.match(regex, url):
        return True
    else:
        return False

def Obfuscation(url):
    oc = od.ObfuscationClassifier(od.PlatformType.ALL)
    classifications = oc([url])
    print(classifications)
    if classifications[0] == 0:
        return True
    else:
        return False

