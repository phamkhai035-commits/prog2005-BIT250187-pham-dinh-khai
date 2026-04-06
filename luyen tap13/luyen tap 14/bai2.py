n = int(input("Nhập n: "))

for i in range(n):
    print("* " * n)

for i in range(1, n + 1):
    print("* " * i)

for i in range(n, 0, -1):
    print("* " * i)

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "*")

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)


for i in range(1, n + 1):
    print(" " * (n - i) + "*" + (" " * (2*i-3) + "*" if i > 1 else ""))

for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" + (" " * (2*i-3) + "*" if i > 1 else ""))
