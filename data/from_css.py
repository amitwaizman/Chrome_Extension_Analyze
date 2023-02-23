import re

# find url
def return_all_urls_in_css(css):
    # Find all URLs
    # urls = re.findall(r"url\(['\"]?(.*?)['\"]?\)", css, re.IGNORECASE)
    urls = re.findall(r"url\(['\"]?(https?:)?\/\/.*?['\"]?\)", css, re.IGNORECASE)
    # if len(urls) > 0:
    #     print(urls)
    return urls
    # Print each URL
    # for url in urls:
    #     print(url)

def check_css_for_script_like_code(css):
    # Check for script-like code
    if re.search(r":\s*[\w\-]+\s*\(\s*['\"].*?\)", css):
        return True
    return False

def check_css_for_malicious_code(css):
    # Check for base64 encoded strings
    if re.search(r"url\(data:text\/plain;base64,[a-zA-Z0-9\/\+=]+?\)", css):
        return True
    
    # Check for comment obfuscation
    if re.search(r"\/\[\s\S]?\*\/", css):
        return True
    
    # Check for character escaping
    if re.search(r"\w\\[0-9a-fA-F]{2}", css):
        return True
    
    # Check for long, random strings
    if re.search(r"[\w\-\.\#]+\{[\s\S]{500,}\}", css):
        return True
    
    # Check for suspicious CSS properties
    if re.search(r"(expression|javascript|eval|vbscript|behaviour|@import|@charset)", css, re.IGNORECASE):
        return True
    
    return False