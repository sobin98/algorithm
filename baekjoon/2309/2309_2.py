height=[int(input()) for _ in range(9)]
breaker=False

for i in range(8):
	for j in range(i+1,9):
		if sum(height)-height[i]-height[j]==100:
			a=height[i]
			b=height[j]
			breaker=True
			break
	if breaker==True:
		break

height.remove(a)
height.remove(b)
height.sort()

for i in height:
	print(i)
