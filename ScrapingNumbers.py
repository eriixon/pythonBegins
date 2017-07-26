
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_4598.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sumTags = 0
for tag in tags:
    #Look at the parts of a tag
    print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Attrs:', tag.attrs)
    print('Contents:', tag.contents[0])
    sumTags += int(tag.contents[0])

print (sumTags)