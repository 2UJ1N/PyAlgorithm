#
# 2869
# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import math

a, b, v = map(int, input().split())

day = (v - b) / (a - b)
print(math.ceil(day))