from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import json

f = open("forex.html")
soup = BeautifulSoup(f.read(), "html.parser")

table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('style') and tag['style']=="border-collapse:separate;border-spacing:1px;max-width:1264px;margin:0 auto") 
rawData = table.findAll("td", {"class": "body-table"})
rows = []
for i in rawData:
      i = i.contents[0]
      cleanr = re.compile('<.*?>')
      i = re.sub(cleanr, '', (str)(i))
      rows.append(i)

reshaped = []
json_data = []
for i in range(0, 10):
    row = rows[(i*12):(i*12)+12]
    reshaped.append(row)
    json_data.append({'No.' : (int)(row[0]), 'Ticker': row[1], 'Price' : row[2], 'Perf 5Min' : row[3], 'Perf Hour' : row[4], 'Perf Day' : row[5], 'Perf Week' : row[6], 'Perf Month' : row[7], 'Perf Quart' : row[8], 'Perf Half' : row[9], 'Perf Year' : row[10], 'Perf YTD' : row[11]})

f = open("data.json", "w")
f.write(json.dumps(json_data))
f.close()

print("Done")