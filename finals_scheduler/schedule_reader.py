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

                #[row['Course 1'], row['Course 2'], row['Course 3'], row['Course 4'],
                                       #row['Course 5'], row['Course 6']]

                # todo not sure if using objects for courses anymore
                #student_courses = []

                for student_course_num in student_course_nums:
                    if student_course_num is not None:
                        if student_course_num not in courses:
                            courses.append(student_course_num)

                        if student_course_num not in conflicts:
                            # Conflicts should be all of the courses that are in the list besides the current course, as it is the first entry
                            conflicts[student_course_num] = [x for i, x in enumerate(student_course_nums)
                                                             if i != student_course_nums.index(student_course_num)]
                        else:
                            course_conflicts = conflicts[student_course_num]
                            # Add conflicts to the existing course
                            # Should be all courses besides the current one and that are not already in the list
                            # todo test this
                            course_conflicts.append([x for i, x in enumerate(student_course_nums)
                                                     if i != student_course_nums.index(student_course_num)
                                                     and x not in course_conflicts])
                            conflicts[student_course_num] = course_conflicts

                students.append(Student(row['Lastname'], row['Firstname'], student_course_nums))


                '''
                    student_courses.append(Course(student_course_num))

                if len(courses) != 0:
                    for course in courses:
                        for student_course in student_courses:
                            if course.course_num == student_course.course_num:
                                course.add_conflict_courses(student_courses[student_courses.index(student_course):len(student_courses)])


                    # Handle first course, there are no conflicts yet
                    if len(courses) == 0:
                        courses.append(Course(student_course_num))
                    else:
                        for course in courses:
                            # If we already have the course, just add it to the student list
                            if course.course_num == student_course_num:
                                student_courses.append(course)
                            # otherwise, it is a new course and we must create it
                            else:
                                new_course = Course(student_course_num)
                                courses.append(new_course)
                                student_courses.append(new_course)

                print(row['Lastname'], row['Firstname'])
                students.append(Student(row['Lastname'], row['Firstname'], student_courses))
            '''

        return students, courses, conflicts
