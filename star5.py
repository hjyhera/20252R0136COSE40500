import random
import time

n = 5
colors = ['\033[31m', '\033[32m', '\033[33m']  # red, green, yellow 
reset = '\033[0m'

for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = ''
    for _ in range(2 * i - 1):
        color = random.choice(colors)
        stars += color + '*' + reset
    print(spaces + stars)