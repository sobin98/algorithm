n,E,W,N,S=map(int,input().split())
plane=[[0]*(2*n) for _ in range(2*n)]

total_percent=0

def back_tracking(x,y,cnt,percent):
	global total_percent
	plane[x][y]=1
	if cnt==n:
		total_percent+=percent
		
	else:
		now=percent
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			
			if plane[nx][ny]==1:
				continue
			else:
				back_tracking(nx,ny,cnt+1,now*percents[i])
				plane[nx][ny]=0
	return total_percent
				


dx=[1,-1,0,0]
dy=[0,0,1,-1]
percents=[E*0.01,W*0.01,N*0.01,S*0.01]
back_tracking(0,0,0,1)

print(total_percent)
