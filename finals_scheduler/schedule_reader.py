import csv
from student import Student
from course import Course


class ScheduleReader():

    def __init__(self, schedules_csv):
        self.schedules_csv = schedules_csv

    def read_schedules(self):
        with open(self.schedules_csv, newline='') as fp:
            reader = csv.DictReader(fp)
            students = []
            courses = []
            conflicts = {}

            for row in reader:
                # get the course numbers for the current student
                student_course_nums = []
                for i in range(1, 7):
                    course_num = row['Course {}'.format(str(i))]
                    if course_num is not None:
                        student_course_nums.append(course_num)

                # todo not sure if using objects for courses anymore
                #student_courses = []

                for student_course_num in student_course_nums:
                    if student_course_num is not None:
                        if student_course_num not in courses:
                            courses.append(student_course_num)

                        if student_course_num not in conflicts:
                            # Conflicts should be all of the courses that are in the list besides the current course,
                            # as it is the first entry
                            conflicts[student_course_num] = [x for i, x in enumerate(student_course_nums)
                                                             if i != student_course_nums.index(student_course_num)]
                        else:
                            course_conflicts = conflicts[student_course_num]
                            # Add conflicts to the existing course
                            # Should be all courses besides the current one and that are not already in the list
                            course_conflicts.append([x for i, x in enumerate(student_course_nums)
                                                     if i != student_course_nums.index(student_course_num)
                                                     and x not in course_conflicts])
                            conflicts[student_course_num] = course_conflicts

                students.append(Student(row['Lastname'], row['Firstname'], student_course_nums))

        return students, courses, conflicts
