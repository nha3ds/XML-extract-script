

def cleanXml(xml):
    return xml.replace("\n", " ")

def cleanXmls(xmls):
    cleanedXmls = []
    for xml in xmls:
        cleanedXml = cleanXml(xml)
        cleanedXmls.append(cleanedXml)
    return cleanedXmls

def getXmls (file_path):
    wordStart = "<DataEntry"
    wordEnd = "</DataEntry"
    with open(file_path,'r') as f:
        started = False
        singleXml = ""
        xmlList = []
        lineNum = 0
        for line in f:
            
            line = str(line)
            lineNum += 1
            if (lineNum % 10000) == 0:
                print("file: "+file_path+"   read line:" + str(lineNum))
            
            try:
                a = line.index(wordStart)
                startOfXml = line[a:]
                singleXml = startOfXml
                started = True

                try:
                    a = line.index(wordEnd)
                    started = False
                    xmlList.append(singleXml)
                except:
                    started = True
                    continue

            except:
                pass

            if started:
                try:
                    a = line.index(wordEnd)
                    endOfXml = line[:a]
                    singleXml = singleXml+endOfXml
                    started = False
                    xmlList.append(singleXml)
                except:
                    singleXml = singleXml+line
        return (xmlList)


