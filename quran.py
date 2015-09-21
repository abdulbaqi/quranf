#!usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/<int:chapter>/<int:verse>')
def renderq(chapter,verse):
	return "here is chapter %d verse %d"%(chapter,verse)
 
@app.route('/')
def index():
	return "hello world"

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)  
