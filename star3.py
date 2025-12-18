n = 5
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '\033[32m' + '*' * (2 * i - 1) + '\033[0m'  # green stars
    print(spaces + stars)