import sys
INF=sys.maxsize

#노드의 개수 및 간선의 개수를 입력받기
n=int(input())
m=int(input())

#2차원 리스트로 만들고 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기자신에서 자기자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
	for j in range(1,n+1):
		if i==j:
			graph[i][j]=0

#각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
	a,b,c=map(int,input().split())
	if graph[a][b]>c:
		graph[a][b]=c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#수행된 결과를 출력
for a in range(1,n+1):
	for b in range(1,n+1):
		#도달할수 없는경우
		if graph[a][b]==INF:
			print(0,end=" ")
		#도달할수 있는경우
		else:
			print(graph[a][b],end=" ")

	print()
