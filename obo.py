# obo.py

def stripTags(pagecontents):
    startLoc = pagecontents.find("<hr/><h2>")

    pagecontents = pagecontents[startLoc:]
    return pagecontents
