import sys
import classes.api as api
# import classses.scheduler as sc

def main():
	queries = sys.argv
	courses = {}
	for i in range (1, len(sys.argv)):
		currCourse = sys.argv[i].upper()
		print sys.argv[i].upper()
		courses[currCourse] = api.get_course_data(currCourse)
		print courses

	# scheduler = sc.Scheduler(courses)
main()