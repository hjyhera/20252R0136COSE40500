n = 5
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    if i == 1:
        stars = '\033[33m' + '*' * (2 * i - 1) + '\033[0m'  # yellow star for top
    else:
        stars = '\033[32m' + '*' * (2 * i - 1) + '\033[0m'  # green stars
    print(spaces + stars)