import math
import ast
import glob
import json
import csv
from pprint import pprint

data = []
for filename in glob.glob('../server/submissions/*.json'):
    #print(filename)
    with open(filename) as f:
        json_data = ast.literal_eval(f.read())
        for x in range(0,15):
            temp = {}
            #print(json.dumps(json_data[x]))
            user = int(json_data[x]["userAnsV1"])
            actual = int(json_data[x]["actualAnsV1"])
            logError = math.log2(abs(user-actual) + 1/8)
            if(logError < 0):
                temp["logError"] = 0
            else:
                temp["logError"] = logError
            temp["type"] = json_data[x]["graphType"]

            data.append(temp)
print(data)

# modified from http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/

output = open('compiledData.csv', 'w')
csvwriter = csv.writer(output)


count = 0
for row in data:
    if count == 0:
        header = row.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(row.values())
output.close()

