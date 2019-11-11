
class Course():

    def __init__(self, course_num):
        self.course_num = course_num
        self.conf_courses = []

    def add_conflict_course(self, conf_courses):
        for conf_course in conf_courses:
            if conf_course not in self.conf_courses:
                conf_course.append(conf_course)
            else:
                #todo remove
                print("Course {} already conflicts with: {}".format(self.course_num, conf_course.course_num))

