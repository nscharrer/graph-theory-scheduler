from schedule_reader import ScheduleReader


def main():
    scheduleReader = ScheduleReader("C:\\Users\\scharrernf\\Documents\\Fall_2019\\MA327\\major_project\\schedules.csv")
    students, courses, conflicts = scheduleReader.read_schedules()




main()
