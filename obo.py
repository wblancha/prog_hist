# obo.py

def stripTags(pagecontents):
    startLoc = pagecontents.find("<hr/><h2>")

    pagecontents = pagecontents[startLoc:]

    
    inside = 0
    text = ""
 
    for char in pagecontents:
        if char == "<":
            inside = 1
        elif (inside == 1 and char == ">"):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text      
def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)
