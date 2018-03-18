# encoding: UCS-2
import requests
import re
content=requests.get('https://book.douban.com/').text
print(content)
                   
