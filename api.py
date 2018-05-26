import re
import json
import requests

import classes.course as course

payload = { 'key': '737f0946481560fccacc9ec4afd0c3c1' } 
api = 'https://api.uwaterloo.ca/v2/'
CONST_UW = "UW U"

def get_courses_by_substr(substr):
	
	if substr == '' or not substr:
		return None


	allCourses = json.loads(requests.get(url = api + 'courses.json', params = payload).text)

	# get subject, and catalog(if catalog exists)
	substr = substr.upper()
	regex = re.search('^(\D*)(\d+)', substr)
	subject = regex.group(1)
	
	if len(subject) > 4:
		return None
		
	if regex.group(2):
		catalog = regex.group(2)
	else:
		catalog = None
	

	# go through all the courses and find matches based on name and catalog.
	results = []
	if catalog:
		for item in allCourses["data"]:
			name = item["subject"]
			if 

	else:



	relevantCourses = allCourses

def get_time_for_course(crsCode):

	if crsCode == '' or not crsCode:
		return
 
	crsCode = crsCode.upper()
	regex = re.search('^(\D*)(\d+)', crsCode)
	subject = regex.group(1)
	catalog = regex.group(2)


	response = requests.get(url = api + 'courses/' + subject + '/' + catalog + '/schedule.json', params = payload)
	response = json.loads(response.text)

	courses = []
	for item in response["data"]:
		if item["campus"] == "UW U":
			name = item["subject"] + item["catalog_number"]
			date = item["classes"][0]["date"]
			curr = course.Course(name, int(item["class_number"]), date["start_time"], date["end_time"])
			courses.append(curr)
	print courses[1].classNumber



def test_get_time_for_course(crsCode):
	get_time_for_course(crsCode)



test_get_time_for_course("MATH235")