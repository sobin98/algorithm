n=int(input())
steps=[0]*301

for i in range(n):
	steps[i]=int(input())
	
dp=[0]*n

dp[0]=steps[0]
dp[1]=steps[0]+steps[1]
dp[2]=steps[2]+(max(steps[0],steps[1]))

for i in range(3,n):
    dp[i]=max(dp[i-2]+steps[i],dp[i-3]+steps[i-1]+steps[i])

print(dp[n-1])
