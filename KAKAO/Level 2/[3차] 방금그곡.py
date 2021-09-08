"""2018 KAKAO BLIND RECRYITMENT"""


def time_minus(start, end):
    start_h, start_m = start.split(":")
    end_h, end_m = end.split(":")

    if start_m <= end_m:
        return (int(end_h) - int(start_h)) * 60 + int(end_m) - int(start_m)
    return (int(end_h) - int(start_h) - 1) * 60 + 60 - (int(start_m) - int(end_m))


def solution(m, musicinfos):
    answer = ""
    music_infos = []
    for musicinfo in musicinfos:
        temp = musicinfo.split(",")
        playing_time = time_minus(temp[0], temp[1])

        if playing_time % len(temp[3]) == 0:
            code = temp[3] * (playing_time // len(temp[3]))
        elif len(temp[3]) < playing_time:
            code = (
                temp[3] * (playing_time // len(temp[3]))
                + temp[3][: playing_time % len(temp[3])]
            )
        else:
            code = temp[3][: playing_time % len(temp[3])]

        music_infos.append([playing_time, temp[2], code])
    music_infos.sort(key=lambda x: (-x[0]))

    for music_info in music_infos:
        if m in music_info[2]:
            return music_info[1]

    return "(None)"
