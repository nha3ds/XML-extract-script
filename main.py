from find_xml import getXmls
from find_xml import cleanXmls
from find_xml_type import isCorrectSubType
from extract_xml_data import xmlTypeOne
from extract_xml_data import getXmlTypeOneHeaders
from bs4 import BeautifulSoup
# Import Module
import os
import sys
import datetime
import json

dataHeaders = getXmlTypeOneHeaders
isCorrectXml = isCorrectSubType
dataRow = xmlTypeOne

outputFile = ""
inputPath = ""
searchName = ""
configFile = "config.json"
isProd = False

if len(sys.argv) > 1:
    configFile = sys.argv[1]

if len(sys.argv) > 2:
    isProd = sys.argv[2]

with open(configFile, 'r') as f:
    data = json.load(f)
    outputFile = data["output"]
    inputPath = data["input"]
    searchName = data["search"]

# Change the directory
cwd = os.getcwd()
os.chdir(inputPath)
fileList = os.listdir()
os.chdir(cwd)
output = dataHeaders()
ct = datetime.datetime.now()

print(outputFile)

f = open(outputFile, "w")
for line in output:
    lineText = ""
    for cell in line:
        lineText = lineText + cell+","
    lineText = lineText[:-1]
    f.write(lineText+'\n')
f.close()
# iterate through all file
for file in fileList:
    # Check whether file is in text format or not
    if file.startswith(searchName):
        file_path = f"{inputPath}/{file}"
        # call read text file function
        print(file_path)
        old_xmls = getXmls(file_path)
        xmls = cleanXmls(old_xmls)
        lineNum = 0
        for xml in xmls:
            lineNum = lineNum+1
            if (lineNum % 10000) == 0:
                print("file: "+file_path+"   exported xml:" + str(lineNum))
            if isCorrectXml(xml):
                soup = BeautifulSoup(xml, 'xml')
                singleOutput = dataRow(soup)
                lineText = ""
                for cell in singleOutput:
                    lineText = lineText + cell + ","

                lineText = lineText[:-1]
                f = open(outputFile, "a")
                f.write(lineText + '\n')
                f.close()


print(outputFile)
print("time started: "+str(ct.hour)+"-"+str(ct.minute))
ct = datetime.datetime.now()
print("time finished:"+str(ct.hour)+"-"+str(ct.minute))
