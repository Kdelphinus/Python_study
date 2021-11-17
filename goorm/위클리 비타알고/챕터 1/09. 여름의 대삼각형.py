# 신발끈 정리 설명 : https://ladyang86.tistory.com/60
def shoelace_formula(coor1, coor2, coor3):
    """shoelace_formula 신발끈 정리를 이용한 함수

    Args:
        coor1 (tuple): 주어진 좌표
        coor2 (tuple): 주어진 좌표
        coor3 (tuple): 주어진 좌표
    """
    left_to_right = coor1[0] * coor2[1] + coor2[0] * coor3[1] + coor3[0] * coor1[1]
    right_to_left = coor1[0] * coor3[1] + coor3[0] * coor2[1] + coor2[0] * coor1[1]
	
    return abs(left_to_right - right_to_left) / 2


coor1 = tuple(map(int, input().split()))
coor2 = tuple(map(int, input().split()))
coor3 = tuple(map(int, input().split()))
print('%.2f' %shoelace_formula(coor1, coor2, coor3))
