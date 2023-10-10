# Set and Dictionary(+ List, Tuple)
이보다 더 자세한 내용들은 모두 [파이썬 공식 문서](https://docs.python.org/ko/3/tutorial/datastructures.html) 에 있다.

## 0. 목차
1. [List](#1-list)
   1. [Declaration](#11-declaration)
   2. [Indexing and Slicing](#12-indexing-and-slicing)
   3. [List function](#13-list-function)
2. [Tuple](#2-tuple)
   1. [Declaration](#21-declaration)
   2. [Tuple function](#22-tuple-function)
3. [Dictionary](#3-dictionary)
   1. [Declaration](#31-declaration)
   2. [Dictionary function](#32-dictionary-function)
   3. [defaultdict](#33-defaultdict)
4. [Set](#4-set)
   1. [Declaration](#41-declaration)
   2. [Set function](#42-set-function)


## 1. List
List는 파이썬이 제공하는 시퀀스 자료구조이다.
stack, queue, deque를 구현할 때 자주 사용되며 c의 배열과 가장 흡사하다.

list는 여러 원소들로 구성되어 있으며, 문자열처럼 각 원소들에 순서가 인덱스로 저장된다. 
그렇기에 인덱스를 통해 각 원소들을 불러올 수 있다. 

### 1.1 Declaration
리스트는 []로 데이터들을 감싸며 선언한다. 
안에는 문자, 정수 등 다양한 자료형이 들어갈 수 있다. 

빈 리스트는 다음과 같이 생성할 수 있다. 
```python
a = []
b = list()
```

그리고 직접 값을 넣어서 다양한 자료형의 리스트, 혹은 이중 리스트도 생성할 수 있다.
```python
a = [1, 2, 3]
b = ["Life", "is", "short", "You", "need", "Python"]
c = [1, 2, "Python"]
d = [1, 2, ["Life", "Python"]]
```

### 1.2 Indexing and Slicing
앞서 이야기했듯 리스트는 각 원소마다 인덱스를 가지고 있기에 indexing과 slicing이 가능하다.
이때 index는 0부터 시작한다.

인덱싱으로 값을 불러오는 동작은 다음과 같다.
```shell
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> a[0]
1
```

또한 인덱싱으로 불러온 값들의 연산도 가능하다.
```shell
>>> a[0] + a[2]
4

>>> b = ["Life", "is", "short", "You", "need", "Python"]
>>> b[0] + " " +  b[-1]
Life Python
```
이때, 음수의 인덱스는 맨 뒤의 값부터 접근한다. (시작은 -1부터)


이중 리스트에선 인덱스를 두 개 사용하여 원하는 값에 접근도 가능하다.
```shell
>>> a = [1, 2, [5, 2, 3, 4]]
>>> a[0]
1

>>> a[2]
[5, 2, 3, 4]

>>> a[2][1]
2
```

slicing은 임의의 특정 범위를 가져올 때 사용한다.

변수 뒤에 [start:end:step]를 지정한다. 
- start: 시작 인덱스
- end: 끝 인덱스, 이때 end 인덱스의 값은 포함하지 않는다.
- step: 인덱스간의 간격, 선언하지 않으면 자동으로 1이 된다.
```shell
>>> a = [1, 2, 3, 4, 5]
>>> a[0:2]
[1, 2]

>>> a[:2]
[1, 2]

>>> a[2:]
[3, 4, 5]

>>> a[:4:2]
[1, 3]
```

### 1.3 List function
- list.append(x): 리스트의 끝에 x를 추가한다.
- list.count(x): 리스트에서 x가 등장하는 횟수를 반환한다.
- list.sort(*, key=None, reverse=False): 리스트의 항목들을 제자리에서 정렬한다.(옵션은 [정렬 단계의 문서](https://github.com/Kdelphinus/Python_study/tree/main/Baekjoon/solve_step_by_step/11_sort#5-python%EC%9D%98-%EA%B2%BD%EC%9A%B0) 참고)
- len(list): 리스트의 길이(원소들의 개수)를 반환한다.
- 그 외에는 공식 문서 참고

## 2. Tuple
Tuple은 원소들을 ()로 감싸고 있다. 리스트와 비슷하게 원소마다 순서를 가지고 있지만 원소들의 값을 생성, 삭제, 수정할 수 없다.

### 2.1 Declaration
튜플은 원소들을 ()로 감싸서 표현한다. 또한 ()를 사용하지 않고 선언해도 튜블로 선언된다. 
리스트처럼 이중 튜플도 가능하다.

```shell
>>> a = (1, 2, 3)
>>> a
(1, 2, 3)

>>> b = 1, 2, 3
>>> b
(1, 2, 3)

>>> c = (1, 2, ("a", "b", "AB"))
>>> c
(1, 2, ("a", "b", "AB"))
```

### 2.2 Tuple function
튜플 역시 리스트처럼 indexing, slicing이 가능하며 더하거나 곱하기, 길이를 얻는 연산도 동일하게 가능하다.


## 3. Dictionary
Dictionary는 데이터들의 대응관계(key와 value)를 나타낼 수 있는 자료구조이다.

이름 그대로 사전의 역할을 하며 baseball이 야구라는 뜻을 가지듯 key가 value라는 값을 가진다.
그러나 원소들이 순서를 갖진 않으며 key를 통해 value를 얻을 수 있다.

### 3.1 Declaration
딕셔너리는 키와 값의 쌍으로 이루어져있다. 그렇기에 키와 값을 같이 선언해주어야 한다.
```python
dict = {"baseball":"야구", "이닝의 개수":9}

dict2 = {"a":[1, 2, 3, 4], 1:"pyhotn"} 
```

딕셔너리에 원소를 추가할 땐 키를 인덱스로 값을 입력하면 된다.
```shell
>>> dict = {"a":"ㄱ"}
>>> dict["b"] = "ㄴ"
>>> dict
{"a":"ㄱ", "b":"ㄴ"}
```

또한 삭제 시, del을 이용하여 삭제하면 된다. (이는 list에서도 동일하다.)
```shell
>>> dict = {"a":"ㄱ", "b":"ㄴ"}
>>> del dict["b"]
>>> dict
{"a":"ㄱ"}
```

만약 같은 키값을 넣으면 마지막 키의 값만 기억한다. 또한 키값으로 튜플은 사용할 수 있지만 리스트는 사용할 수 없다.
```shell
>>> a = {1:"a", 1:"b"}
>>> a
{1:"b"}
```

### 3.2 Dictionary function
- dict.key(): 딕셔너리의 key만 모아서 dict_key 객체로 돌려준다.
- dict.values(): 딕셔너리의 value만 모아서 dict_value 객체로 돌려준다.
- dict.items(): key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
- 그 외의는 공식 문서 참고

### 3.3 defaultdict
파이썬의 딕셔너리는 지정하지 않은 키를 연산으로 이용하면 에러가 난다. 
그러나 collections 모듈에 있는 defaultdict을 이용하면 지정하지 않은 키가 들어오면 default값으로 자동 지정해준다.

```python
from collections import defaultdict

int_dict = defaultdict(int)
int_dict["A"]
int_dict["B"] = 2

-> int_dict = {"A":0, "B":2}
```
int를 default로 정의하면 지정되지 않은 키를 선언할 때, 자동으로 0을 값으로 할당한다.

그 외에도 list, set을 기본값으로 지정할 수 있으며 이는 키와 값을 초기해주고 사용해야 하는 기존 딕셔너리의 번거로움을 줄일 수 있다.

## 4. Set
Set은 집합과 관련한 연산들을 쉽게 처리하기 위해서 만들어진 자료구조다. 
set은 중복을 허용하지 않으며 순서가 없다.

### 4.1 Declaration
set은 원소를 {}로 감싼 형태로 표현한다. 
```shell
>>> s1 = set([1, 2, 3])
>>> s1
{1, 2, 3}

>>> s2 = set("hello")
>>> s2
{"h", "e", "l", "o"}
```

### 4.2 Set function
```python
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8, 9])
```

- 교집합 &, intersection()
```shell
>>> s1 & s2
{4, 5}

>>> s1.intersection(s2)
{4, 5}
```

- 합집합 |, union()
```shell
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
```

- 차집합 -, difference()
```shell
>>> s1 - s2
{1, 2, 3}

>>> s1.difference(s2)
{1, 2, 3}

>>> s2 - s1
{6, 7, 8, 9}
```
- set.add(x): x원소를 set에 추가
- set.update([x, y, z]): 여러 개의 원소를 한 번에 추가
- set.remove(x): 특정 값을 제거
