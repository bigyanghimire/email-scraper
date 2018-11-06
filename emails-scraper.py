import re
from bs4 import BeautifulSoup as bs
import requests
import lxml
import csv
url=https://www.quora.com
str=requests.get(url).text
parsed_html=bs(str,'lxml')
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) 
    ## ['alice@google.com', 'bob@abc.com']    
for email in emails:
    # do something with each found email string
    print(email)
