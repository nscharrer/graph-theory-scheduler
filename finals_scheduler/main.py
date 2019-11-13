from schedule_reader import ScheduleReader
import grapher


def main():
    scheduleReader = ScheduleReader("E:\\Documents\\MSOE\\Fall_2019\\MA327\\major_project\\graph-theory-scheduler\\schedules.csv")
    students, courses, conflicts = scheduleReader.read_schedules()

    colored_dict = grapher.greedy_coloring(conflicts)
    grapher.graph_courses(colored_dict)
    #grapher.graph_tester1()


main()
