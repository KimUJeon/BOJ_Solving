import sys
from itertools import combinations

while True:
	testcase = list(map(int, sys.stdin.readline().rstrip().split()))
	if testcase[0] == 0:
		break

	testcase.pop(0)

	for combi in combinations(testcase, 6):
		res = list(map(str, combi))
		print(" ".join(res))
	print()

# 아래 코드는 하려다 망함, 시간을 들이면 어떻게 완성될 것 같기는 한데 코드 상태를 봐서는 시간제한 걸릴듯
# while True:
# 	testcase = list(map(str, sys.stdin.readline().rstrip().split()))
# 	if testcase[0] == '0':
# 		break
# 	else:
# 		testcase.pop(0)
# 		temp_testcase = testcase[0:6]
# 		idx = 4
# 		stop = 0
# 		while idx >= 0:
# 			for item in testcase[(idx+1):(len(testcase)-stop)]:
# 				if item > temp_testcase[idx]:
# 					temp_testcase[idx+1] = item
# 					print(temp_testcase)
# 			print("한번끝")
# 			idx -= 1
# 			stop += 1

# DFS 풀이 방식

