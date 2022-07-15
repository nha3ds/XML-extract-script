def cleanNoneTypes(txt):
    if txt is None:
        return ""
    return txt

def cleanCommas(txt):
    return txt.replace(',',' ')

def cleanText(txt):
        txt1 = cleanNoneTypes(txt)
        txt2 = cleanCommas(txt1)
        return txt2

def cleanAllText(arr):
    for i in range(len(arr)):
            arr[i] = cleanText(arr[i])
    return arr

def xmlTypeOne(soup):
    singleOutput = [soup.EntryId.attrs.get("id"),
                                soup.Timestamp.attrs.get("date"), soup.Timestamp.attrs.get("time"),soup.Person.attrs.get("id")]
    singleOutput = cleanAllText(singleOutput)
    return singleOutput

def getXmlTypeOneHeaders():
    return [["EntryId.id","Timestamp.date","Timestamp.time","Person.id"]]


