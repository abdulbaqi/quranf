from collections import OrderedDict
class QError(RuntimeError):
	pass


class Q:


 def __init__(self):
	file = open('quran-uthmani-min.txt','r')
	self.data=OrderedDict()

	for line in file:
	 lsplit = line.split('|')
	 chapter, verse ,text = lsplit[0], lsplit[1],lsplit[2]
	 self.data[chapter+':'+verse]=text

 def get(self,id='1:1'):
	if id not in self.data:
	  raise QError('not a valid verse no.')
	return self.data[id]



 def gsura(self, id='1'):
	result = []
	found = False
	for key in self.data:
		if id == key.split(':')[0]:
	          result.append(key.split(':')[1]+"-"+self.data[key])
		  found = True
	if not found:
	 raise QError('not a valid sura')
	return result
