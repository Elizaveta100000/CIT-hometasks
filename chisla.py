n = 10000
a = [0] * n
for i in range(n):
    a[i] = i

a[1] = 0

m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1
c = 0
 # вывод простых чисел
for i in a:
    if a[i] != 0 and c<1000:
        c = c + 1
        print(a[i])