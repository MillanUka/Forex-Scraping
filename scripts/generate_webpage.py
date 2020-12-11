from jinja2 import Environment, FileSystemLoader
import json

def generate_table(data):
    html = """<table>
    <tr>
    <th>No.</th>
    <th>Ticker</th>
    <th>Price</th><th>Perf 5Min</th><th>Perf Hour</th><th>Perf Day</th><th>Perf Week</th><th>Perf Month</th><th>Perf Quart</th><th>Perf Half</th><th>Perf Year</th><th>Perf YTD</th></tr>"""
    print(data.pop(0))
    for row in data:
        html += "<tr>"
        for i in row:
            html += "<td>" + str(row[i]) + "</td>"
        html += "</tr>"
    return html + "</table>"

templateLoader = FileSystemLoader(searchpath="./templates")
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = "index.template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

with open('data.json') as json_file:
    rawData = json.load(json_file)
    data = {
        'date_updated': rawData[0],
        "table" : generate_table(rawData)
        }
    f = open("index.html", "w")
    f.write(template.render(data=data))
    f.close()

