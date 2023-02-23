#baekjoon_10162.py
#Greedy

sec = int(input())

button = [0, 0, 0]
time = 0

button[0] = sec // 300
time = sec % 300
button[1] = time // 60
time = time % 60
button[2] = time // 10
time = time % 10

if time > 0:
    print(-1)
elif button[0]==0 and button[1]==0 and button[2] == 0:
    print(0)
else:
    print(button)

    
# 11053
N = int(input())
A = list(map(int, input().split(' ')))

dp = [0] * len(A)

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


#baekjoon_11055.py
#DP

num = 10 # int(input())
arr = [1, 100, 2, 50, 60, 30, 5, 6, 7, 8]  # list(map(int, input().split()))

dp = arr[:]

for i in range(num):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(dp)
