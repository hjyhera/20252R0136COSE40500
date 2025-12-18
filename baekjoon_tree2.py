# Baekjoon 16468

import sys

def solve():
    # 입력: 볼의 개수 N, 높이 L
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
    n = int(input_data[0])
    l = int(input_data[1])
    
    MOD = 100030001
    
    # S[i][j]: 노드 i개로 높이 j 이하인 이진트리를 만드는 경우의 수
    # 행: 노드 개수(0~N), 열: 높이(0~L)
    S = [[0] * (l + 1) for _ in range(n + 1)]
    
    # 노드가 0개이면 어떤 높이에서도 경우의 수는 1 (빈 트리)
    for j in range(l + 1):
        S[0][j] = 1
        
    # DP 진행
    for j in range(1, l + 1): # 높이를 1부터 L까지 증가
        for i in range(1, n + 1): # 노드 개수를 1부터 N까지 증가
            count = 0
            # 왼쪽 자식에 k개, 오른쪽 자식에 i-1-k개 배분
            for k in range(i):
                left = S[k][j-1]
                right = S[i-1-k][j-1]
                count = (count + (left * right)) % MOD
            S[i][j] = count
            
    # 결과 출력: (높이 L 이하인 경우) - (높이 L-1 이하인 경우)
    # 음수가 나올 수 있으므로 MOD를 더한 후 나머지 연산
    ans = (S[n][l] - S[n][l-1] + MOD) % MOD
    print(ans)

solve()