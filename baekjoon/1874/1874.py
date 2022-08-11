k=int(input())

in_stack=[] #주어진 수열을 저장하기 위한 리스트 (그림의 왼쪽부분)
out_stack=[] #스택구현 (그림의 오른쪽부분)
printst=[]

for _ in range(k):
	in_stack.append(int(input()))
in_stack=in_stack[::-1]

for i in range(k):
	out_stack.append(i+1)
	printst.append('+')
	
	if in_stack[-1]==out_stack[-1]:
		while (len(out_stack)!=0) and (in_stack[-1]==out_stack[-1]):

			printst.append('-')
			in_stack.pop()
			out_stack.pop()

if len(out_stack)==0:
	print('\n'.join(printst))
else:
	print("NO")
