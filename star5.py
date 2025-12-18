import random
import time

n = 5
colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']  # red, green, yellow, blue, magenta, cyan
reset = '\033[0m'

while True:
    print('\033[2J\033[H')  # clear screen
    for i in range(1, n+1):
        spaces = ' ' * (n - i)
        stars = ''
        for _ in range(2 * i - 1):
            color = random.choice(colors)
            stars += color + '*' + reset
        print(spaces + stars)
    time.sleep(0.5)  # blink every 0.5 seconds