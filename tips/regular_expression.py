"""정규표현식(정규식)
- 복잡한 문자열을 처리할 때 사용하는 기법
- 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용"""


"""문자 클래스 []
* [abc]: a, b, c 중 한 개의 문자와 매치
    "a": 매치
    "before": 매치
    "dude': 매치되지 않음

* '-'을 사용하면 두 문자 사이의 범위 전체를 의미
    [a-zA-Z]: 알파벳 전체
    [0-9]: 숫자

* 앞에 '^'은 not을 의미
    [^a-z^A-Z]: 알파벳을 제외한 나머지 문자
    [^0-9]: 숫자를 제외한 나머지 문자

* 자주 사용하는 문자 클래스의 별도 표기법
    \d - 숫자와 매치, [0-9]와 동일한 
    \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식
    \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미
    \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식
    \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식
    \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식
"""


"""Dot .
* 줄바꿈 문자('\n')를 제외한 모든 문자와 매치됨을 의미
    - re.DOTALL 옵션을 주면 '\n'과도 매치됨

* a.b
    - a와 b 사이에 어떤 문자가 들어가도 모두 매치됨을 의미
    - "aab": a와 b 사이에 a가 있으므로 매치
    - "a0b": a와 b 사이에 0이 있으므로 매치
    - "abc": a와 b 사이에 문자가 하나도 없기에 매치되지 않음

* a[.]b
    - 문자 클래스 내에 dot이 들어가면 이는 모든 문자가 아닌 문자 그대로의 '.'을 의미
    - "a.b": 매치
    - "a0b": 가운데 '.'이 없으므로 매치되지 않음
"""


"""반복
* ca*t
    - {0,}과 동일
    - '*' 바로 앞에 있는 a가 0부터 무한대로(실제론 메모리 제한으로 2억개 정도만 가능) 반복될 수 있다는 의미
    - "ct", "cat", "caaat" 모두 매치

* ca+t
    - {1,}과 동일
    - '+'는 앞의 문자가 최소 1번 이상 반복될 때 매치
    - "cat", "caaat"는 매치되지만 "ct"는 매치되지 않음

* ca{m}t
    - 반드시 m번만큼 반복되는 것만 매치
    - ca{2}t -> "caat"만 매치

* ca{m, n}t
    - m부터 n까지 반복만 매치
    - ca{2, 5}t -> "caat", "caaaaat"는 매치되지만 "cat"는 매치되지 않음

* ?
    - {0, 1}과 같은 의미
    - 즉, 있어도 되고 없어도 된다
    - ca?t -> "cat", "ct"는 매치
"""


import re

p = re.compile("[a-z]+")  # 컴파일된 패턴 객체

"""match
문자열의 처음부터 정규식과 매치되는지 조사"""
m = p.match("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>

m = p.match("3 python")
print(m)  # None, 매치되지 않기 때문

# 파이썬 정규식 기본 흐름
# p = re.compile(정규표현식)
# m = p.match( 'string goes here' )
# if m:
#    print('Match found: ', m.group())
# else:
#    print('No match')

# -------------------------------------------------------------------------------------------------

"""search
문자열 전체가 정규식과 매치되는지 조사"""
m = p.search("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>

m = p.search("3 python")
print(m)  # <re.Match object; span=(2, 8), match='python'>, 2 ~ 8인덱스만 매치됨을 보여줌

# -------------------------------------------------------------------------------------------------

"""findall
정규식과 매치되는 단어들을 리스트로 돌려준다"""
result = p.findall("life is too short")
print(result)  # ['life', 'is', 'too', 'short']

result = p.findall("3 python")
print(result)  # ['python']

result = p.findall("3")
print(result)  # []

# -------------------------------------------------------------------------------------------------

"""finditer
findall과 동일하지만 리스트대신 반복 가능한 객체를 돌려준다"""
result = p.finditer("life is too short")
print(result)  # <callable_iterator object at 0x000002B3EA47BE20>

for r in result:
    print(r)
"""<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>"""

result = p.finditer("3 python")
print(result)  # <callable_iterator object at 0x00000236BB26BF10>

for r in result:
    print(r)  # <re.Match object; span=(2, 8), match='python'>

# -------------------------------------------------------------------------------------------------

"""match 객체의 메소드"""
m = p.match("python")
print(m.group())  # python, 매치된 문자열
print(m.start())  # 0, 매치된 문자열의 시작 위치
print(m.end())  # 6, 매치된 문자열의 끝 위치
print(m.span())  # (0, 6), 매치된 문자열의 (시작, 끝)에 해당하는 튜플

m = p.search("3 python 2 abc")  # 매치되는게 여러 군데 있으면 가장 앞에 있는 단어만 가져옴
print(m.group())  # python
print(m.start())  # 2
print(m.end())  # 8
print(m.span())  # (2, 8)

# -------------------------------------------------------------------------------------------------

"""모듈 단위로 수행"""
p = re.compile("[a-z]+")
m = p.match("python")

m = re.match("[a-z]+", "python")  # 위의 과정을 이렇게도 쓸 수 있음

# -------------------------------------------------------------------------------------------------

"""컴파일 옵션
DOTALL(S) - '.'이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)"""

# DOTALL
p = re.compile("a.b")
m = p.match("a\nb")
print(m)  # None

p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)  # <re.Match object; span=(0, 3), match='a\nb'>


# IGNORECASE, I
p = re.compile("[a-z]", re.I)
print(p.match("python"))  # <re.Match object; span=(0, 1), match='P'>
print(p.match("Python"))  # <re.Match object; span=(0, 1), match='P'>
print(p.match("PYTHON"))  # <re.Match object; span=(0, 1), match='P'>


# MULTILINE, M
p = re.compile("^python\s\w+")  # 'python'이 맨 앞에 오고 그 뒤에 공백, 그 뒤에 단어가 와야 한다는 의미

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # ['python one']

p = re.compile("^python\s\w+", re.MULTILINE)  # 각 라인을 처음으로 인식시킴

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # ['python one', 'python two', 'python three']

p = re.compile("\w+\spython$", re.MULTILINE)  # python이 맨 뒤에 오고 그 앞에 공백, 그 앞엔 단어들이 나옴

data = """python one
life is too short
python two
you need python
python three
using python"""

print(p.findall(data))  # ['need python', 'using python']

# -------------------------------------------------------------------------------------------------

"""VERBOSE, X

밑에 있는 두 개의 compile은 동일한 작동을 하지만 주석이 달린 것이 훨씬 가독성이 좋다
re.VERBOSE를 사용하면 입력되는 문자열의 whitespace는 제거된다([]안에 있는 whitespace는 제외
#을 이용하여 각 줄에 주석을 달 수 있다"""
charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")

charref = re.compile(
    r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""",
    re.VERBOSE,
)

# -------------------------------------------------------------------------------------------------

"""백슬래시 문제"""
# '\section'을 찾아야 할 때

p = re.compile("\section")  # \s + ection을 찾게된다
p = re.compile("\\section")  # 파이썬 리터럴 규칙에 따라 \\이 \으로 변경됨, 즉 위와 같은 결과를 가져옴
# 위 같은 경우는 파이썬에서 정규식을 사용할 때만 발생, 파이썬 리터럴 규칙 때문

p = re.compile("\\\\section")  # 이렇게해야 '\section'을 찾는다. 그러나 가독성이 너무 떨어짐
p = re.compile(r"\\section")  # '\section'을 찾음, 정규식 앞에 r을 쓰는 것으로 raw string 규칙을 적용

# -------------------------------------------------------------------------------------------------

"""그 외 메타문자들"""
# |, or의 의미
p = re.compile("Crow|Servo")
m = p.match("CrowHello")
print(m)  # <re.Match object; span=(0, 4), match='Crow'>


# ^, 문자열 처음과 매치함을 의미
print(
    re.search("^Life", "Life is too short")
)  # <re.Match object; span=(0, 4), match='Life'>
print(re.search("^Life", "My Life"))  # None


# $, 문자열 끝과 매치함을 의미
print(
    re.search("short$", "Life is too short")
)  # <re.Match object; span=(12, 17), match='short'>
print(re.search("short$", "Life is too short, you need python"))  # None


# \A
# ^와 같은 의미
# re.MULTILINE을 사용해도 줄과 상관없이 전체 문자열 중 처음하고만 매치


# \Z
# $와 같은 의미
# re.MULTILINE을 사용해도 줄과 상관없이 전체 문자열 중 끝하고만 매치


# \b, 단어 구분자
# 리터럴 규칙에 영향을 받지 않도록 r을 붙여 raw string임을 보여주어야 한다
p = re.compile(r"\bclass\b")  # whitespace로 구분되는게 일반적
print(p.search("no class at all"))  # <re.Match object; span=(3, 8), match='class'>
print(p.search("declassified AI"))  # None, class가 있으나 whitespace로 구분되지 않았기 때문
print(p.search("one subclass is"))  # None, class가 있으나 whitespace로 구분되지 않았기 때문


# \B, whitespace로 구분되지 않은 단어만 매치
p = re.compile(r"\Bclass\B")  # whitespace로 구분되지 않은 단어만 찾음
print(p.search("no class at all"))  # None, whitespace로 구분되어 있기 때문
print(p.search("declassified AI"))  # <re.Match object; span=(2, 7), match='class'>
print(p.search("one subclass is"))  # None, whitespace가 하나라도 있기 때문

# -------------------------------------------------------------------------------------------------

"""Grouping"""
p = re.compile("(ABC)+")  # ABC를 grouping해서 반복되는지 확인
m = p.search("ABCABCABC OK?")
print(m)  # <re.Match object; span=(0, 9), match='ABCABCABC'>

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")  # 이름과 번호, 국번을 각각 grouping
m = p.search("park 010-1234-5678")
print(m.group(0))  # park 010-1234-5678, 매치된 전체 문자열
print(m.group(1))  # park, 첫 번째 그룹에 해당되는 문자열
print(m.group(2))  # 010-1234-5678, 두 번째 그룹에 해당되는 문자열
print(m.group(3))  # 010, 그룹을 중첩하여 사용하면 안으로 들어갈수록 인덱스가 증가


# grouping된 문자열 재참조하기
# 두 번째 그룹을 참조하려면 마지막에 \2를 사용하면 된다
p = re.compile(r"(\b\w+)\s+\1")  # '(그룹) + " " + 그룹과 동일한 단어'와 매치
print(p.search("Paris in the the spring"))  # the the, 동일한 단어가 두 번 나온 the와 매치


# grouping된 문자열에 이름 붙이기
# (?P<그룹명>...)으로 확장구문을 사용하여 이름을 붙인다
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")  # 첫번째 그룹에 name이라는 이름을 붙임
m = p.search("park 010-1234-1234")
print(m.group("name"))

# 재참조할 때는 (?P=그룹명)으로 재참조한다
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")  # 첫번째 그룹에 word라는 이름을 붙이고 재참조
print(p.search("Paris in the the spring").group())

# -------------------------------------------------------------------------------------------------

"""전방 탐색
긍정형 전방 탐색((?=...)) - ...에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다
부정형 전방 탐색((?!...)) - ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다

.*[.].*$ - '파일 이름 + . + 확장자'를 나타내는 정규식
    - 확장자가 bat인 파일을 제외하고 확장자가 3글자가 아니여도 작동하게 만들면
    - .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ - 긍정형 전방 탐색으로 만들었을 때
    - .*[.](?!bat$).*$ - 부정형 전방 탐색으로 만들었을 때

bat과 exe 두 개를 제외하라는 조건으로 만들면
    - .*[.](?!bat$|exe$).*$
"""
# 긍정형 전방 탐색
p = re.compile(".+(?=:)")  # ':' 앞까지만 탐색
m = p.search("http://google.com")
print(m.group())  # http

# -------------------------------------------------------------------------------------------------

"""문자열 바꾸기"""
p = re.compile("(blue|white|red)")
# sub("바꿀 문자열", "대상 문자열")
print(p.sub("color", "blue socks and red shoes"))  # color socks and color shoes
# count를 넣으면 바꾸기 횟수를 제어할 수 있음
print(p.sub("color", "blue socks and red shoes", count=1))  # color socks and red shoes


# subn은 ("바뀐 문자열", "바꾼 횟수")의 튜플로 리턴
print(
    p.subn("color", "blue socks and red shoes")
)  # ('colour socks and colour shoes', 2)


# sub 메소드 사용 시 참조 구문 사용
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-5678"))  # 010-1234-5678 park

# -------------------------------------------------------------------------------------------------

"""Greedy vs Non-Greedy"""

# * 등의 메타 문자는 탐욕스러워서 매치할 수 있는 최대한의 문자열을 모두 소비한다
s = "<html><head><title>Title</title>"
print(re.match("<.*>", s).span())  # (0, 32)
print(re.match("<.*>", s).group())  # <html><head><title>Title</title>


# ?를 사용하여 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할
print(re.match("<.*?>", s).group())  # <html>
