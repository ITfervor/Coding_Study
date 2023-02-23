# 3:30 퀴즈
for i in range(1, 51):
    with open( str(i) + "주차 보고서.txt", "w", encoding="utf8") as work_file:
        work_file.write("- {0} - 주차 주간 보고".format(i))
        work_file.write("\n부서 : ")
        work_file.write("\n이름 : ")
        work_file.write("\n업무요약 : ")
    