numbers = list(map(int, input().split()))

print(*sorted(numbers, key=abs, reverse=True))
