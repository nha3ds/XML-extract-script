from bs4 import BeautifulSoup
def isCorrectSubType(xml):
    soup = BeautifulSoup(xml, 'xml')
    val = soup.find_all(attrs={"subType": "update"})
    if len(val) > 0:
        return True
    else:
        return False




