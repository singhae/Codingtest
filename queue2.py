import sys 
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])

for _ in range(N):
    func = sys.stdin.readline().split()
    if func[0] == "push":
        queue.append(func[1])
    elif func[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif func[0] == "size":
        print(len(queue))
    elif func[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif func[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif func[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
