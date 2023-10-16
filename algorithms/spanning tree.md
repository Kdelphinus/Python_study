# Spanning Tree

## Spanning Tree(신장 트리)

### 특징

- 그래프의 최소 연결 부분 그래프
- n개의 노드을 가지면 그래프의 간선은 (n - 1)개만 존재한다.
- 즉, 그래프에서 일부 간선을 선택해서 만든 트리
- 스패닝 트리는 특수한 형태이므로 **모든 노드들이 연결**되어 있어야 하며 **사이클을 포함하면 안 된다.**

### 사용 사례

- 통신 네트워크 구축에서 사용된다.
- 예시) 회사 내의 모든 전화기를 가장 적은 수의 케이블을 사용하여 연결

## Minimum Spanning Tree(MST, 최소 신장 트리)

### 특징

- 스패닝 트리 중 사용된 간선들의 가중치 합이 최소인 트리
- 통신망, 도로망, 유통망의 비용을 최소로 구축하려는 경우에 사용

### 구현 방법

#### 1. Kruskal MST 알고리즘

**탐욕적인 방법**을 이용하는 알고리즘

- 순서
    1. 그래프들의 간선을 가중치의 오름차순으로 정렬
    2. 정렬된 간선 리스트에서 차례대로 사이클을 형성하지 않는 간선을 택한다.

    - 즉, 가장 낮은 가중치를 먼저 택한다.
    - 사이클을 형성하는 간선은 제외한다.

    3. 해당 간선을 현재의 MST 집합에 추가한다.

```python

```

#### 2. Prim MST 알고리즘

시작 노드부터 시작해서 신장트리 집합을 **단계적으로 확장** 해나가는 방법

- 순서
    1. 시작 단계에서는 시작 노드만이 MST 집합에 포함된다.
    2. 이전 단계에서 만들어진 MST 집합에 인접한 노드들 중에서 최소 간선으로 연결된 노드를 선택하여 트리를 확장한다.

    - 즉, 가장 낮은 가중치를 먼저 선택한다.

    3. 위 과정을 (n - 1)개의 간선이 만들어질 때까지 반복한다.

```python
import sys
import heapq

INPUT = sys.stdin.readline


def prim() -> int:
    cnt, weight = 0, 0
    heap = [[0, 1]]

    while heap:
        if cnt == V:
            return weight

        w, s = heapq.heappop(heap)
        if not VISITED[s]:
            VISITED[s] = True
            weight += w
            cnt += 1
            for i in GRAPH[s]:
                heapq.heappush(heap, i)


if __name__ == "__main__":
    V, E = map(int, INPUT().split())
    VISITED = [False for _ in range(V + 1)]
    GRAPH = [[] for _ in range(E)]
    for _ in range(E):
        A, B, C = map(int, INPUT().split())
        GRAPH[A].append((C, B))
        GRAPH[B].append((C, A))
    print(prim())
```

**Kruskal 알고리즘**은 간선들을 정렬하기에 일반적으로 간선이 적으면 **Kruskal**, 많으면 **Prim** 알고리즘을 사용한다.

## 참고 문헌

- [Heee's Development Blog, [알고리즘] 최소 신장 트리(MST, Minimum Spanning Tree)란](https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html)
- [hillier_house, [백준 1197] 최소 스패닝 트리 (python)](https://hillier.tistory.com/54)