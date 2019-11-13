import csv


class Scheduler():
    def __init__(self, course_dict, students, slot_filename="default_slots.csv", student_filename="default_students.csv"):
        self.course_dict = course_dict
        self.students = students
        self.slot_filename = slot_filename
        self.student_filename = student_filename
        self.course_exam_slots = {}

    def write_exam_slots(self):
        schedule_dict = {}
        for course in self.course_dict:
            conflicts, color = self.course_dict[course]
            if color in schedule_dict:
                no_conflict_courses = schedule_dict[color]
                no_conflict_courses.append(course)
                schedule_dict[color] = no_conflict_courses
            else:
                schedule_dict[color] = [course]

        with open(self.slot_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            time_slot = 0
            for color in schedule_dict:
                exam_slot = 'Exam Slot {}'.format(time_slot)
                row = [exam_slot]
                courses = schedule_dict[color]
                for course in courses:
                    row.append(course)
                    self.course_exam_slots[course] = exam_slot
                writer.writerow(row)
                time_slot += 1

    def write_student_schedules(self):

        with open(self.student_filename, 'w', newline='') as csvfile:
            fieldnames = ['Lastname', 'Firstname', 'Course 1', 'Course 1 Slot', 'Course 2', 'Course 2 Slot',
                          'Course 3', 'Course 3 Slot', 'Course 4', 'Course 4 Slot', 'Course 5', 'Course 5 Slot',
                          'Course 6', 'Course 6 Slot']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student in self.students:
                row_dict = {'Lastname': student.lastname, 'Firstname': student.firstname}
                for i in range(len(student.courses)):
                    row_dict['Course {}'.format(i+1)] = student.courses[i]
                    row_dict['Course {} Slot'.format(i+1)] = self.course_exam_slots[student.courses[i]]
                writer.writerow(row_dict)
