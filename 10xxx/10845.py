N = int(input())

arr = []

for _ in range(N):
    inp = input().split()
    match inp[0]:
        case "push":
            arr.append(inp[1])
        case "pop":
            if len(arr) > 0:
                print(arr.pop(0))
            else:
                print(-1)
        case "size":
            print(len(arr))
        case "empty":
            print(int(len(arr) == 0))
        case "front":
            if len(arr) > 0:
                print(arr[0])
            else:
                print(-1)
        case "back":
            if len(arr) > 0:
                print(arr[-1])
            else:
                print(-1)
