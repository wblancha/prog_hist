# html-to-list.py

import urllib2, obo

url = "http://www.oldbaileyonline.org/print.jsp?div=t17800628-33"

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html)
wordlist = text.split()
print wordlist[0:120]
