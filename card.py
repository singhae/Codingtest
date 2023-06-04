import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

i = 1
for i in range(1, N+1):
    q.append(i)

while True:
    if len(q) == 1:
        break
    q.popleft()
    q1 = q[0]
    q.popleft() 
    q.append(q1)

print(q[0])