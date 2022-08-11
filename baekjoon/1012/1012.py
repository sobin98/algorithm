import sys
sys.setrecursionlimit(10 ** 4)
t=int(input())

answer=[]
def dfs(x,y):
	#범위 벗어나는 경우에 false
	if x<0 or y<0 or x>=n or y>=m:
		return False
    #배추가 있는 부분과 이어진부분은 모두 true
	if graph[x][y]==1:
		graph[x][y]=0
		dfs(x,y+1)
		dfs(x,y-1)
		dfs(x-1,y)
		dfs(x+1,y)
		return True
    #범위도 벗어나지 않고 배추가 없으면 false    
	return False
	
for _ in range(t):
	m,n,k=map(int,input().split())
	graph=[[0]*m for _ in range(n)]
	result=0

	for _ in range(k):
		a,b=map(int,input().split())
		graph[b][a]=1

	for i in range(m):
		for j in range(n):
			if dfs(j,i)==True:
				result+=1
	answer.append(str(result))
	

print('\n'.join(answer))
