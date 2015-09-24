#Quran on Flask

This tutorial renders the Quranic text through a flask framework for illustrative purposes.

#v0.1 

The read me file creation

#v0.2

establish the basic framework. 

Display 'hello world' at the root address

also, display the url to listen on all ports '0.0.0.0', in my case the link is

http://data-abdulbaqi.c9.io

#v0.3

added a new route (/chapter/verse) with a mock message

#v0.4 - working solution

This version does a significant improvement over the last version.

It brought the Quranic text from http://tanzil.net/download/

It then created a new py file called `q.py` which contans Q class to load the Quran into a dictionary and a function within this class to return a verse given its number.

#v0.5 - templates

Here I created templates folder and made two templates.

Note the special handling of utf-8 unicode in the main quran.py file. 


#v0.6 - Error handlind

created `QError` class in `q.py` and made necessary adjustment in the main `quran.py` file

also, added a license file

#v0.7 - Display Surah

I have introduced a new URL route `(/chapter)` which will allow users to enter a sura number and the whole sura will be displayed. In order to do that, I had to change the data type of the Quran into an `OrderedDict`. Also a new template is created. 
