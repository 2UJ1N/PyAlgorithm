#
# 5086
# 배수와 약수
# https://www.acmicpc.net/problem/5086

while 1:
    a, b = map(int, input().split())

    if a == 0 and b == 0: exit()
    else:
        if b % a == 0: print("factor")
        elif a % b == 0: print("multiple")
        else: print("neither")