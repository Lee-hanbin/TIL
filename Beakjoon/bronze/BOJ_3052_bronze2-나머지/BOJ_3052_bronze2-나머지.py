# BOJ 3052 bronze2 나머지

import sys

set1 = set()
for i in sys.stdin:
    if i == '\n':
        break
    set1.add(int(i) % 42)
print(len(set1))