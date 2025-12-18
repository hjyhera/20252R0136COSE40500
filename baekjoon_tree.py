# Baekjoon 1234

import sys

memo = {}

fact = [1] * 11
for i in range(2, 11):
    fact[i] = fact[i-1] * i

def solve(lv, r, g, b, N):
    # 모든 레벨을 다 채운 경우
    if lv > N:
        return 1
    
    state = (lv, r, g, b)
    if state in memo:
        return memo[state]
    
    res = 0
    
    # 1. 한 가지 색만 사용하는 경우
    if r >= lv: res += solve(lv + 1, r - lv, g, b, N)
    if g >= lv: res += solve(lv + 1, r, g - lv, b, N)
    if b >= lv: res += solve(lv + 1, r, g, b - lv, N)
    
    # 2. 두 가지 색을 사용하는 경우 (lv가 2로 나누어 떨어져야 함)
    if lv % 2 == 0:
        cnt = lv // 2
        comb = fact[lv] // (fact[cnt] * fact[cnt])
        if r >= cnt and g >= cnt: res += solve(lv + 1, r - cnt, g - cnt, b, N) * comb
        if r >= cnt and b >= cnt: res += solve(lv + 1, r - cnt, g, b - cnt, N) * comb
        if g >= cnt and b >= cnt: res += solve(lv + 1, r, g - cnt, b - cnt, N) * comb
            
    # 3. 세 가지 색을 사용하는 경우 (lv가 3으로 나누어 떨어져야 함)
    if lv % 3 == 0:
        cnt = lv // 3
        comb = fact[lv] // (fact[cnt] * fact[cnt] * fact[cnt])
        if r >= cnt and g >= cnt and b >= cnt:
            res += solve(lv + 1, r - cnt, g - cnt, b - cnt, N) * comb
            
    memo[state] = res
    return res

# 입력
n, r, g, b = map(int, sys.stdin.readline().split())

# 장난감 총합이 트리 완성에 필요한 개수보다 적으면 0 출력
if n * (n + 1) // 2 > r + g + b:
    print(0)
else:
    print(solve(1, r, g, b, n))