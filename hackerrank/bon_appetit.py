n, k = map(int, input().split())
a = list(map(int, input().split()))
b = int(input())

x = sum(a) - a[k]
if 2 * b ==x:
    print("Bon Appetit")
else:
    print(a[k] // 2)