class QError(RuntimeError):
	pass


class Q:


 def __init__(self):
	file = open('quran-simple-clean.txt','r')
	self.data={}

	for line in file:
	 lsplit = line.split('|')
	 chapter, verse ,text = lsplit[0], lsplit[1],lsplit[2]
	 self.data[chapter+':'+verse]=text

 def get(self,id='1:1'):
	if id not in self.data:
	  raise QError('not a valid verse no.')
	return self.data[id]

