from collections import deque

queue = deque()

N = int(input())

for i in range(N):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())