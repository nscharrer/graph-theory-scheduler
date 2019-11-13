import csv


def write_schedules(course_dict, filename="default_schedule.csv"):
    schedule_dict = {}
    for course in course_dict:
        conflicts, color = course_dict[course]
        if color in schedule_dict:
            no_conflict_courses = schedule_dict[color]
            no_conflict_courses.append(course)
            schedule_dict[color] = no_conflict_courses
        else:
            schedule_dict[color] = [course]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        time_slot = 0
        for color in schedule_dict:
            row = ['Exam Slot {}'.format(time_slot)]
            courses = schedule_dict[color]
            for course in courses:
                row.append(course)
            writer.writerow(row)
            time_slot += 1

    return 0
