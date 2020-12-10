import json
f = open("./forex.html", "r")
jsonData = json.dumps(f.read())
f = open('data.json', 'w') 
f.write(jsonData)
f.close() 

