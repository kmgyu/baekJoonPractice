# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N, M = map(int, input().split())
mat = [input() for _ in range(N)]

direction = [
	[1, 0],
	[-1, 0],
	[0, 1],
	[0, -1],
	[1, 1],
	[1, -1],
	[-1, -1],
	[-1, 1]
]

HQ = [] # start, S
ant = [] # antenna
dest = [] # destination, E
# ene = [] # enemy

for i in range(N):
	for j in range(M):
		if mat[i][j] == 'S':
			HQ = (i,j)
		elif mat[i][j] == '.':
			ant.append((i,j))
		elif mat[i][j] == 'E':
			dest = (i,j)
		# 브루트 포스 방식 쓸까 저장해둘까 했는데
		# 몇개라는 제한도 없어서 차라리 단방향 브루트포스 탐색이 나을 것 같음.
		# elif mat[i][j] == '#':
		# 	ene.append((i,j))

edges = dict()

def find(coord):
	x, y = coord
	edges = []
	for mx, my in direction:
		cx, cy = x, y
		weight = 0
		while 0<=cx<N and 0<=cy<M:
			cx, cy = cx+mx, cy+my
			if not (0<=cx<N and 0<=cy<M): break
			if mat[cx][cy] in ('S', 'E', '.'):
				edges.append([weight+1, (cx, cy)])
				break
			elif mat[cx][cy] == '#': break
			weight += int(mat[cx][cy])
	return edges

nodes = [HQ] + ant

for node in nodes:
	edges[node] = find(node)

from heapq import heappush, heappop
from collections import defaultdict

dist = defaultdict(lambda: float('inf'))
def dijikstra(coord):
	q = []
	heappush(q, (0, coord))
	dist[coord] = 0
	while q:
		d, node = heappop(q)
		for weight, next in edges[node]:
			if dist[next] > d + weight:
				dist[next] = d + weight
				heappush(q, (d + weight, next))
	return dist

print(dijikstra(HQ)[dest])