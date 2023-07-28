import sys
from collections import defaultdict
"""
투 포인터 문제
right로 올라가다가 k 값에 도달하면 left를 움직여서
최댓값 탐색
"""
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

left = 0
right = 0
counts = defaultdict(int)
res = 0

while right < n:
    counts[l[right]] += 1
    while counts[l[right]] > k:
        counts[l[left]] -= 1
        left += 1
    res = max(res, right - left + 1)
    right += 1

print(res)




