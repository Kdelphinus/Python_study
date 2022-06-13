import os

# currentPath = os.getcwd()

# print(currentPath)
# os.chdir("C:/Users/delphinus/Desktop/Workspace/Python")

"""
파일 경로 지정할 때, 터미널 창에 나오는 곳이 작업 폴더이니 참고할 것
"""

os.getcwd()  # 현재 경로
os.chdir("지정하고 싶은 경로")  # 경로 설정
os.listdir()  # 현재 폴더의 디렉토리 리스트
os.path.dirname("경로")  # 파일명을 제외하고 경로만 가져옴
os.path.dirname(os.path.realpath(__file__))  # 현재 파일이 있는 폴더의 경로
os.path.basename("경로")  # 파일명만 가져옴
os.path.isfile("경로")  # 파일인지 확인하여 bool 리턴
os.path.isdir("경로")  # 폴더인지 확인하여 bool 리턴
dir, file = os.path.split("경로")  # dir엔 경로, file엔 파일 이름이 저장됨
os.path.exists("경로")  # 파일 또는 디렉토리 경로 존재 유무 확인

# 그 외 기능들 : https://ddolcat.tistory.com/654
