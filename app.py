from flask import Flask,request
from bs4 import BeautifulSoup
import collections
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return "Server is Live"

@app.route('/parse-html',methods = ['POST'])
def parseHtml():
  
  payload = request.json
  parsed_html = BeautifulSoup(payload["inputHtml"],'html.parser')
  listOfNodes = parsed_html.find("html").find_all(recursive=True)
  duplicates = []

  # Get duplicates from list of nodes
  for node, count in collections.Counter(listOfNodes).items():
    if count > 1:
      duplicates.append({"node":str(node),"count":count,"name":node.name})

  # Condition to check if duplicate is already present due to parent being present
  for i in duplicates:
    temp = i["node"]
    for j in duplicates:
      t2 = j["node"]
      if (t2 in temp) and (i["count"] == j["count"]) and i!=j:
        duplicates.remove(j)

  # Convert response to json
  jsonResponse = json.dumps(duplicates)
  return jsonResponse


if __name__ == '__main__':
  app.run(debug=True)
