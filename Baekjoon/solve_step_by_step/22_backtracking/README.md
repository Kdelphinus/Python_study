# **Backtracking**

## 0. Index
1. [개요](#1-개요)
2. [DFS와 BFS](#2-dfs와-bfs)
3. [가지치기(Pruning)](#3-가지치기pruning)
4. [최선 우선 탐색](#4-최선-우선-탐색)

## 1. 개요
```Backtracking```은 모든 경우의 수 중 특정한 조건을 만족하는 경우의 수(가지치기를 통해)를 전부 고려하는 알고리즘으로 완전 탐색이라고 할 수 있다. 
특히 상태공간을 트리로 나타낼 수 있을 때, 적합하며 일종의 트리 탐색 알고리즘으로 볼 수도 있다. 
방식에 따라 ```DFS```와 ```BFS```가 있다. 이에 대해선 이후 단계에서 나올 때 더 자세히 살펴볼 예정이다.

## 2. DFS와 BFS
간단하게만 살펴보면 ```DFS```는 트리에서 바닥에 도달할 때까지, 즉 막다른 길에 도착하거나 정답에 도달할 때까지 들어가고 막다른 길에 도착하면 되돌아 나와서 다른 방향을 탐색하는 방법이다. 
```BFS```는 모든 분기점을 다 살펴보는 방식이다.

일반적으로 DFS는 재귀, BFS는 큐를 사용하는데 DFS가 좀 더 빠른 편에 속한다. 그러나 트리의 깊이가 무한대라면 DFS로는 답을 구할 수 없기에 BFS를 사용해야 한다.

## 3. 가지치기(Pruning)
가지치기는 해를 찾는 과정 중에 지금의 경로가 해가 될 가능성이 없다고 판단될 때, 그 경로를 더 이상 가지 않는 것을 의미한다. 
즉, 불필요한 경로를 조기에 차단하여 경우의 수를 줄이는 것이라고 보면 된다. 

예를 들어 n-queen의 경우, queen이 겹치는 상황에 놓이면 그 후의 경우의 수는 보지 않고 다음 경우의 수로 넘어가는 것이 가지치기라고 할 수 있다. 

## 4. 최선 우선 탐색
BFS를 좀 더 발전시킨 형태인 최선 우선 탐색(Best First Search)은 큐 대신 우선순위 큐(보통은 힙으로 구현)를 사용한다. 
새로운 경우를 순차적으로 탐색하는 BFS와 다르게 현재 가장 최적인 경우를 우선적으로 탐색하기에 상대적으로 효율적이다. 
이는 해결하지 못할 때를 제외하고는 효율적으로 해결할 수 있는 장점이 있다. 

거기다가 무의미한 탐색을 막을 가지치기를 적용한다면 꽤나 효율적인 탐색을 할 수 있다. 