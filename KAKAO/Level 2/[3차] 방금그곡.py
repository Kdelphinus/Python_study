"""2018 KAKAO BLIND RECRYITMENT"""


def time_minus(start, end):
    """time_minus 두 시간의 차이를 구하는 함수

    Args:
        start (str): 시작 시간, "HH:MM"으로 주어짐
        end (str): 종료 시간, "HH:MM"으로 주어짐

    Returns:
        (int): 두 시간의 차이
    """
    start_h, start_m = start.split(":")
    end_h, end_m = end.split(":")

    if start_m <= end_m:
        return (int(end_h) - int(start_h)) * 60 + int(end_m) - int(start_m)
    return (int(end_h) - int(start_h) - 1) * 60 + 60 - (int(start_m) - int(end_m))


def solution(m, musicinfos):
    """solution 무슨 노래인지 찾아주는 함수

    Args:
        m (str): 들었던 노래의 코드
        musicinfos (list): 노래의 "시작시간, 종료시간, 제목, 악보"들이 담긴 리스트

    Returns:
        (str): 들은 노래의 제목
    """
    music_infos = []
    for musicinfo in musicinfos:
        temp = musicinfo.split(",")  # 정보들을 각각 나눈다
        playing_time = time_minus(temp[0], temp[1])  # 재생된 시간을 구한다
        song_len = len(temp[3]) - temp[3].count("#")  # 실제 노래의 길이를 구한다
        codes = []
        idx = 0
        while idx < len(temp[3]):  # 노래의 코드를 저장한다
            if idx < len(temp[3]) - 1 and temp[3][idx + 1] == "#":
                codes.append(temp[3][idx : idx + 2])
                idx += 2
            else:
                codes.append(temp[3][idx])
                idx += 1

        code = temp[3] * (playing_time // song_len)  # 노래가 돌아간만큼 붙여준다
        if playing_time % song_len:  # 노래가 중간에 종료되었다면
            for i in range(playing_time % song_len):  # 재생된 만큼만 붙여준다
                code += codes[i]

        music_infos.append([playing_time, temp[2], code])  # 노래의 정보를 저장한다

    music_infos.sort(key=lambda x: (-x[0]))  # 재생시간이 긴 순서대로 정렬한다
    for music_info in music_infos:
        if music_info[2].count(m) > music_info[2].count(m + "#"):  # 구하는 코드가 있다면
            return music_info[1]  # 노래 제목을 리턴

    return "(None)"  # 찾는 노래가 없다면 (None)을 리턴


# ----------------------------------------------------------------------------------------------------------
"""두 글자 코드를 한 글자로 바꾸어 풀은 코드"""


def shap_to_lower(s):
    s = (
        s.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
    )
    return s


def solution(m, musicinfos):
    answer = [0, "(None)"]  # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(",")
        time_length = (
            (int(split_info[1][:2]) - int(split_info[0][:2])) * 60
            + int(split_info[1][-2:])
            - int(split_info[0][-2:])
        )
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = (
            part_notes * (time_length // len(part_notes))
            + part_notes[: time_length % len(part_notes)]
        )
        if m in full_notes and time_length > answer[0]:
            answer = [time_length, title]
    return answer[-1]
