from collections import deque

N, K = map(int, input().split())

queue = deque()

for i in range(N):
    queue.append(str(i+1))

ans = []

i = 0
while len(queue) > 0:
    i += 1
    if i == K:
        i = 0
        ans.append(queue.popleft())
    else:
        queue.append(queue.popleft())

print(f"<{', '.join(ans)}>")
