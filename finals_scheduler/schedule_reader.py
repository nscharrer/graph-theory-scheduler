import csv
from student import Student


class ScheduleReader():
    """
    Class to read in schedules of each student from CSV
    """

    def __init__(self, schedules_csv):
        """
        Init the class with the csv to be read
        :param schedules_csv: file with schedules we want to read in
        """
        self.schedules_csv = schedules_csv

    def read_schedules(self):
        """
        Go through each student schedule and compile each course and its conflict as well as the total course
        list and the student object list
        :return: tuple containing: list of students, list of all courses, dictionary of courses and conflicts
        (and empty colors)
        """
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

                # loop through each course that we found
                for student_course_num in student_course_nums:
                    # disregard blank courses (not a full schedule)
                    if student_course_num is not None:
                        # add it to the full course list
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
                            new_conflicts = [x for i, x in enumerate(student_course_nums)
                                                     if i != student_course_nums.index(student_course_num)
                                                     and x not in course_conflicts]
                            # add the new conflicts we found to the list
                            if len(new_conflicts) > 0:
                                for i in range(len(new_conflicts)):
                                    course_conflicts.append(new_conflicts[i])
                            # put it back in the dictionary
                            conflicts[student_course_num] = course_conflicts
                # add a student object to the list
                students.append(Student(row['Lastname'], row['Firstname'], student_course_nums))

        # set all the course colors (second item in the tuple) to None for now, handled later
        for course in conflicts:
            conflicts[course] = (conflicts[course], None)

        return students, courses, conflicts
