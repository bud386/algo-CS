import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
ans = 1
for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            if ans < dp[i]:
                ans = dp[i]

print(ans)
