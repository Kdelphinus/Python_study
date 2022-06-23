t = int(input())
for _ in range(t):
    subject = int(input())
    grades = [list(map(float, input().split())) for _ in range(subject)]
    total_score, total_grade = 0, 0
    for grade, score in grades:
        total_grade += int(grade)
        total_score += grade * score
    print(f"{total_grade} {total_score / total_grade:.1f}")
