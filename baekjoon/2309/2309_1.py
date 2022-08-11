from itertools import combinations

height=[int(input()) for _ in range(9)]

cands=list(combinations(height,7))

for case in cands:
	if sum(list(case))==100:
		answer=sorted(list(case))
		break

for i in answer:
	print(i)
