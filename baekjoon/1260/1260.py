from collections import deque
v,e,s=map(int,input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
	start,end=map(int,input().split())
	graph[start].append(end)
	graph[end].append(start)
	graph[start].sort()
	graph[end].sort()
visit_bfs=[False]*(v+1)
visit_dfs=[False]*(v+1)

def dfs(node):
	visit_dfs[node]=True
	print(node,end=' ')
	for n in graph[node]:
		if not visit_dfs[n]:
			dfs(n)
			
def bfs(node):
	visit_bfs[node]=True
	q=deque([node])

	while q:
		n=q.popleft()
		print(n,end=' ')
		for i in graph[n]:
			if not visit_bfs[i]:
				q.append(i)
				visit_bfs[i]=True
dfs(s)
print()
bfs(s)
