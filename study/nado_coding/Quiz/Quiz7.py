# 매주 1회 작성해야 하는 보고서가 있다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 한다.

# - x 주차 주간보고 - 
# 부서 : 
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 "1주차.txt", ... 으로 만든다.

import pickle 
# for i in range(1,51):
#     with open("{0}주차.txt", "w", encoding="utf8" .format(i)) as report_file:
#         report_file.write("- {0}주차 주간보고- \n부서 : \n이름 : \n업무 요약 : " .format(i))


for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")