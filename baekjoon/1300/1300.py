n=int(input())
k=int(input())

def bs(start,end,k):
	while start<=end:
		mid=(start+end)//2

		cnt=0

		for i in range(1,n+1):
			if mid//i>n:
				cnt+=n
			else:
				cnt+=(mid//i)

		if cnt>=k:
			end=mid-1
		else:
			start=mid+1

	return start
				
print(bs(1,k,k))
