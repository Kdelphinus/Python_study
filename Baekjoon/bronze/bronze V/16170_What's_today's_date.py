import datetime

utc = list(str(datetime.datetime.utcnow().date()).split("-"))
for u in utc:
    print(u)
