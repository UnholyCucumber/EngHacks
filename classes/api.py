import re
import json
import requests

import course as course

payload = { 'key': '737f0946481560fccacc9ec4afd0c3c1' } 
api = 'https://api.uwaterloo.ca/v2/'
CONST_UW = "UW U"


# passing on this since it is not a functional requirement...
def get_courses_by_substr(substr):
	
	if substr == '' or not substr:
		return None

	# all the courses returned from the request
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
	while len(results) < 25:
		if catalog:
			for item in allCourses["data"]:
				name = item["subject"]
				if subject == name and (catalog in item["catalog_number"]):
					results.append(subjects)
	return None



def get_course_data(crsCode):

	if not crsCode:
		return
 
	crsCode = crsCode.upper()
	regex = re.search('^(\D*)(\d+)', crsCode)
	subject = regex.group(1)
	catalog = regex.group(2)


	response = requests.get(url = api + 'courses/' + subject + '/' + catalog + '/schedule.json', params = payload)
	response = json.loads(response.text)

	allSubSections = {}
	currList = []

	for item in response["data"]:
		if item["campus"] == CONST_UW:
			currType = item["section"][:3]

			# if new class type detected, add what we have to the hash, and re-init the list.
			if currList and (currType != currList[-1].classType):
				allSubSections[currList[-1].classType] = currList
				currList = []

			name = item["subject"] + item["catalog_number"]
			date = item["classes"][0]["date"]
			currCourse = course.Course(name, int(item["class_number"]), date["start_time"], date["end_time"], currType)

			currList.append(currCourse)
	allSubSections[currType] = currList

	return allSubSections






def test_get_course_data(crsCode):
	get_course_data(crsCode)
