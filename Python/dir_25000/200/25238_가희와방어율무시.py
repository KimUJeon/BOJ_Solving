import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
print(int(a*(100-b)/100<100))