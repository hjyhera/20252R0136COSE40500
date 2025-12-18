import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
R = int(data[1])
G = int(data[2])
B = int(data[3])

# DP[level][r][g][b] = 경우의 수
# level: 0 to N, r,g,b: 0 to R,G,B
dp = [[[[0 for _ in range(B+1)] for _ in range(G+1)] for _ in range(R+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1

for level in range(1, N+1):
    k = level
    # 각 레벨 k에 대해 가능한 배치
    # 가능한 divisor: k를 나누는 수, 1,2,3 (색이 3개)
    for d in range(1, 4):  # d: 각 색의 장난감 수
        if k % d != 0:
            continue
        c = k // d  # 색의 수, c <= 3
        if c > 3:
            continue
        # 색 조합: 빨강, 초록, 파랑 중 c개를 선택, 각 d개씩
        from itertools import combinations
        colors = ['R', 'G', 'B']
        for comb in combinations(colors, c):
            dr = d if 'R' in comb else 0
            dg = d if 'G' in comb else 0
            db = d if 'B' in comb else 0
            # 이제 dp 업데이트
            for r in range(R - dr + 1):
                for g in range(G - dg + 1):
                    for b in range(B - db + 1):
                        if dp[level-1][r][g][b] > 0:
                            dp[level][r + dr][g + dg][b + db] += dp[level-1][r][g][b]

# 최종 답: dp[N][R][G][B]
print(dp[N][R][G][B])