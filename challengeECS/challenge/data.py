"""Routines associated with the application data.
"""

import json

courses = {}

'''Load the data from the json file.'''
def load_data():    
	f = open('json/course.json',"r")
	l = list(json.loads(f.read()))
	for item in l:
		courses.update({item["id"]:item})
	#print(courses)
	f.close()


