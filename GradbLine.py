import urllib.request, urllib.parse, urllib.error

lines = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in lines:
    print(line.decode().strip())