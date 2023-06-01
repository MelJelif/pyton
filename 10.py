n = int(input())
coins = list(map(int, input("введите положение монет 0 и 1 через пробел: ").split()))

heads = 0
for c in coins:
    if c == 0:
        heads += 1
flips = min(heads, n - heads)

print(flips)
