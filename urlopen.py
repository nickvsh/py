import urllib.request

page = urllib.request.urlopen("http://10.27.3.222/")
text = page.read().decode("utf8")
s = text[233:238]
print("The substring is ", s)
print (page)
print (text)


