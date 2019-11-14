from schedule_reader import ScheduleReader
import grapher
from scheduler import Scheduler
import argparse


def main():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    required.add_argument('-s', '--schedules', metavar='SCHEDULE_FNAME', help='CSV with student schedules to read from')

    optional.add_argument('-e', '--exam_slot_fname', metavar='EXAM_SLOT_FNAME', help='Output filename for exam slots')
    optional.add_argument('-o', '--student_exam_fname', metavar='STUDENT_EXAM_FNAME',
                          help='Output filename for student exam schedules')
    args = parser.parse_args()

    scheduleReader = ScheduleReader(args.schedules)
    students, courses, conflicts = scheduleReader.read_schedules()

    colored_dict = grapher.greedy_coloring(conflicts)
    grapher.graph_courses(colored_dict)

    schedule_maker = Scheduler(colored_dict, students)
    schedule_maker.write_exam_slots()
    schedule_maker.write_student_schedules()


main()
