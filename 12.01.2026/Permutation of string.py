from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(get_permutations("abc"))  
