#
# 2444
# 별 찍기 - 7
# https://www.acmicpc.net/problem/2444

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (i * 2 - 1))
for i in range(1, n):
    print(' ' * i + '*' * (( n - i ) * 2 - 1))