
def find(w, h):
    global dp
    if dp[w][h]: return dp[w][h]
    if w == 0: return 1

    dp[w][h] = find(w - 1, h + 1)

    if h > 0: dp[w][h] += find(w, h - 1)

    return dp[w][h]


while True:
    N = int(input())
    dp = [[False] * (N+1) for _ in range(N+1)]
    if N == 0: break

    print(find(N, 0))
