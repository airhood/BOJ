n = int(input())

a = n//5
a -= (n-5*a)%3

if a == 0:
    print(n//3)
elif a < 0:
    print(-1)
else:
    print(a+(n-5*a)//3)