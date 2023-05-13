import itertools

arr = ['AB', 'BD', 'CF']
print(list(arr))
nPr = itertools.permutations(arr, 3)
print(list(nPr))