# save-webpage.py

import urllib2

url = "http://www.oldbaileyonline.org/print.jsp?div=t17800628-33"

response = urllib2.urlopen(url)
webContent = response.read()

f = open("obo-t17800628-33.html", "w")
f.write(webContent)
f.close()
