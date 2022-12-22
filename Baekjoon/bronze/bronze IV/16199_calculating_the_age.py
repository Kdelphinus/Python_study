year, month, day = map(int, input().split())
t_year, t_month, t_day = map(int, input().split())
flag = False
if t_month > month or (t_month == month and t_day >= day):
    flag = True
print(t_year - year) if flag else print(t_year - year - 1)
print(t_year - year + 1)
print(t_year - year)
