from schedule_reader import ScheduleReader
from grapher import graph_courses


def main():
    scheduleReader = ScheduleReader("C:\\Users\\scharrernf\\Documents\\Fall_2019\\MA327\\major_project\\schedules.csv")
    students, courses, conflicts = scheduleReader.read_schedules()

    graph_courses(conflicts)


main()
