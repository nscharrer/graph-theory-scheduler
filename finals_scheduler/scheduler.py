import csv


class Scheduler():
    """
    Class to create exam schedules and the student final exam schedules
    """

    def __init__(self, course_dict, students, slot_filename="default_slots.csv",
                 student_filename="default_students.csv"):
        """
        Set up the Scheduler with values passed in - should be all initialized by this point
        :param course_dict: dictionary with courses, conflicts, and the course color
        :param students: list of all student objects
        :param slot_filename: file to write out the exam slots
        :param student_filename: file to write out the student final exam schedules
        """
        self.course_dict = course_dict
        self.students = students
        self.slot_filename = slot_filename
        self.student_filename = student_filename
        self.course_exam_slots = {}

    def write_exam_slots(self):
        """
        Write out all the possible final exam slots
        :return: True if the file successfully outputs
        """
        schedule_dict = {}

        # go through all the courses, if it's color already exists in the dictionary, then we want to put it in the same
        # time slot as the other courses of that color
        for course in self.course_dict:
            conflicts, color = self.course_dict[course]
            # if the color already is in the dictionary, we want to add to the same time slot
            if color in schedule_dict:
                no_conflict_courses = schedule_dict[color]
                no_conflict_courses.append(course)
                schedule_dict[color] = no_conflict_courses
            # otherwise this is a new color, i.e. new time slot
            else:
                schedule_dict[color] = [course]

        # write out the data to csv
        with open(self.slot_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            time_slot = 0

            # row for each time slot that we found
            for color in schedule_dict:
                exam_slot = 'Exam Slot {}'.format(time_slot)
                row = [exam_slot]
                courses = schedule_dict[color]

                # add all courses under that color to the row
                for course in courses:
                    row.append(course)
                    self.course_exam_slots[course] = exam_slot

                # write out the row
                writer.writerow(row)
                time_slot += 1

    def write_student_schedules(self):
        """
        Write out the schedules for each student to a csv file
        :return: True if writing is successful
        """
        with open(self.student_filename, 'w', newline='') as csvfile:
            # todo may want to figure out how to make fieldnames based on the input file fieldnames in the future
            fieldnames = ['Lastname', 'Firstname', 'Course 1', 'Course 1 Slot', 'Course 2', 'Course 2 Slot',
                          'Course 3', 'Course 3 Slot', 'Course 4', 'Course 4 Slot', 'Course 5', 'Course 5 Slot',
                          'Course 6', 'Course 6 Slot']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # write out the header line with the fieldnames
            writer.writeheader()

            # Put the data for each student in the following rows
            for student in self.students:
                row_dict = {'Lastname': student.lastname, 'Firstname': student.firstname}

                # add each course that the student is taking to the row_dict as well as the time slot for it
                for i in range(len(student.courses)):
                    row_dict['Course {}'.format(i+1)] = student.courses[i]
                    row_dict['Course {} Slot'.format(i+1)] = self.course_exam_slots[student.courses[i]]

                # write out the row
                writer.writerow(row_dict)
