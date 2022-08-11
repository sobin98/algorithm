n=int(input())
n_arr=list(map(int,input().split(' ')))
m=int(input())
m_arr=list(map(int,input().split(' ')))

n_arr.sort()

def bs(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
for target in m_arr:
	print(bs(n_arr,0,n-1,target))
