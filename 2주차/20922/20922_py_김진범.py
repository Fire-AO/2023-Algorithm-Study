import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
num = defaultdict(int)

m = 0
prev = 0
i = 0
while i < n:
    num[l[i]] += 1
    while num[l[i]] > k:
        num[l[prev]] -= 1
        prev += 1
    m = max(m, i - prev + 1)
    i += 1

print(m)
