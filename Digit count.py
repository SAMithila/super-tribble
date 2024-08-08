def count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // 10
    return cnt

n = 336
print(count(n))