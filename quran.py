#!usr/bin/env python

from flask import Flask, render_template
from q import Q, QError

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
quran = Q()


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<chapter>/<verse>')
def renderq(chapter,verse):
	return render_template('verse.html',verse=quran.get(chapter+':'+verse))

@app.route('/<chapter>')
def renders(chapter):
	return render_template('sura.html', sura=quran.gsura(chapter))

@app.errorhandler(QError)
@app.errorhandler(404)
def runtime_error(e):
 return 'error : this verse does not exist'


if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=False)  
