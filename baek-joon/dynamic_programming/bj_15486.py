N = int(input())

time = [0] * N
price = [0] * N
for i in range(N):
    time[i], price[i] = map(int, input().strip().split(' '))

dp = [0 for _ in range(N)]

# 맨 뒤 계산
if time[N - 1] == 1:
    dp[N - 1] = price[N - 1]

# 맨 뒤의 앞에서 부터
for i in range(N - 2, -1, -1):

    # 해당 날짜에 근무를 했을 때 끝나는 날짜
    day = i + time[i]

    # 해당 날짜에서 근무를 했을때 마지막날에서 끝난다.
    if day == N:
        # 해당 날짜에서 근무해서 끝내는 것 vs 해당 날짜에서 근무하지않고 다른 방법으로 끝내는 것
        dp[i] = max(price[i], dp[i + 1])

    # 해당 날짜에서 근무를 했을 때 마지막날 전에서 끝날 때
    elif day < N:
        # 해당 날짜에서 근무 + 끝난 날짜 이후에서 얻은 최대 금액 vs 포함하지 않는 금액
        dp[i] = max(price[i] + dp[day], dp[i + 1])

    # 해당 날짜에서 근무하면 마지막날 초과
    else:
        # 이 날짜를 포함하지 않는 최대의 금액으로
        dp[i] = dp[i + 1]

print(dp[0])
