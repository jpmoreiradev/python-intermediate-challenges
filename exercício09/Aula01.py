ti = 1, 2, "joao", 3, 4
t2 = 5, 6, 7, 8

t3 = ti + t2

n1, n2, n3, *_, n10 = t3



ti = list(ti)
ti[1] = 300
ti = tuple(ti)
print(ti)
print(t2)
print(*_)