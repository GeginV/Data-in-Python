print('='*5, '12.5.6', '='*5)
L = list(map(float, input('numbers').split()))
print(L)

L[0], L[-1] = L[-1], L[0]
print(L)

L.append(sum(L))
print(L)


