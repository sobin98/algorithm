n,k=map(int,input().split()) 
arr=list(range(1,n+1)) 
index=k-1
result=[]

for i in range(n):
	if index>=len(arr):
		index%=len(arr) 
        result.append(str(arr.pop(index))) 
        index+=(k-1)
	else:
		result.append(str(arr.pop(index)))
		index+=(k-1) 
        
print("<", ", ".join(result), ">", sep='')
