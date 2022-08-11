import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

v,e=tuple(map(int,input().split()))
start=int(input())
graph=[[] for _ in range(v+1)]

for _ in range(e):
	a,b,c=tuple(map(int,input().split()))
	graph[a].append([b,c])

d=[INF]*(v+1)

def dijkstra(start):
	q=[]
	#시작노드로 가기위한 최단경로를 0으로 설정 후 큐에삽입
	heapq.heappush(q,(0,start))
	d[start]=0
	
	while q: #큐가 비어있지 않다면
		#가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
		dist,now=heapq.heappop(q)

		#현재 노드가 이미 처리된 적이 있는 노드라면 무시
		if d[now]<dist:
			continue

		#현재 노드와 연결된 다른 인접한 노드들을 확인
		for j in graph[now]:
			cost=d[now]+j[1]

			#현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost<d[j[0]]:
				d[j[0]]=cost
				heapq.heappush(q,(cost,j[0]))
		

dijkstra(start)

for i in range(1,v+1):
	if d[i]==INF:
		print("INF")
	else:
		print(d[i])
