#!usr/bin/env python

from flask import Flask
from q import Q

app = Flask(__name__)
quran = Q()

@app.route('/<chapter>/<verse>')
def renderq(chapter,verse):
	return quran.get(chapter+':'+verse)
 
@app.route('/')
def index():
	return "hello world"

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)  
