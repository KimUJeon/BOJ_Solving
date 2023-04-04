import sys

N = int(sys.stdin.readline())
nums1 = sorted(list(map(str, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
nums2 = list(map(str, sys.stdin.readline().split()))

result = {}

for i in nums1:
	if i in result:
		result[i] += 1
	else:
		result[i] = 1

for j in nums2:
	if j in result:
		print(result[j], end=' ')
	else:
		print(0, end=' ')

'''
	
'''