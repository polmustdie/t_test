a, b, c, d = (int(i) for i in input().split())
if d - b > 0:
    ans = (d-b)*c
    ans += a
    print(ans)
else:
    print(a)
