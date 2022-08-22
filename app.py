from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Server is Live"

@app.route('/parse-html',methods = ['POST'])
def parseHtml():
  return "Post response"


if __name__ == '__main__':
  app.run(debug=True)