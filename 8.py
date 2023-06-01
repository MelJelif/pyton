n, m, k = map(int, input().split())

if k == n * m - 1:
    print("no")
elif k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")

#не очень понял задачу но вот.