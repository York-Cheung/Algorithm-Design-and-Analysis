# -*- coding:utf-8 -*-
import csv 
import re 

fileHeader = ["Size", "Cost"]

with open("script/nohup.txt", "rb") as textfile:
    line = textfile.readline()
    _Method = ''
    Method = ''
    Size = ''
    Cost = ''
    csvfile = None
    writer = None
    row = []
    while line:
        row = []
        print line,
        match1 = re.match(r'(\S+) sorting:', line)
        match2 = re.match(r'Data size: (\d+) Time cost: (\S+)', line)
        if (match1):
            Method = match1.group(1)
        if (match2):
            row.append(match2.group(1)) 
            row.append(match2.group(2))

        if Method != _Method:
            _Method = Method
            if(csvfile is not None):
                csvfile.close()
            csvfile = open(Method+'.csv','a')
            writer = csv.writer(csvfile)
            writer.writerow(fileHeader)
        if (writer is not None and not csvfile.closed):
            if (row != []):
                writer.writerow(row)
            
        line = textfile.readline()
