"""
u.split("://")을 하면 안 되는 이유

-> 그냥 별 생각없이 "://"으로 split을 시켜버리면 path에 ':'나 '/'가 포함될 수 있기 때문에 틀리기 쉽습니다.
경우를 잘 나눠서 차근차근 풀면 됩니다.
"""


def url_parse(u: str) -> tuple:
    protocol = u.split("://")[0]
    tmp_u = "://".join(u.split("://")[1:]).split("/")
    host_port = tmp_u[0].split(":")
    if len(host_port) == 1:
        host, port = host_port[0], "<default>"
    else:
        host, port = host_port[0], host_port[1]

    if len(tmp_u) == 1:
        path = "<default>"
    else:
        path = "/".join(tmp_u[1:])

    return protocol, host, port, path


def print_url(i: int, u: tuple) -> None:
    print(f"URL #{i}")
    print(f"Protocol = {u[0]}")
    print(f"Host     = {u[1]}")
    print(f"Port     = {u[2]}")
    print(f"Path     = {u[3]}")
    print()


if __name__ == "__main__":
    num = int(input())
    for idx in range(1, num + 1):
        url = input()
        print_url(idx, url_parse(url))

"""
정규식 풀이
링크: https://velog.io/@youngcheon/%EB%B0%B1%EC%A4%80-6324-URLs-Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D

import re
output = ["Protocol = ",'Host     = ','Port     = ','Path     = ']
for i in range(1, int(input())+1):
    s = input()
    p = re.match('(http|ftp|gopher)://([\\w.-]+)(?::([\\d]+))?(?:/([\\S]+))?',s)
    print(f"URL #{i}")
    for j, k in enumerate(output,1):
        print(f"{k}{p.group(j)}".replace("None","<default>"))
    print()
"""
