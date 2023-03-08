


def stringPermutation(s):
    out= []

    # Base Case
    if len(s)==1:
        out=[s]
        
    else:
        for i, let in enumerate(s):
            for perm in stringPermutation(s[:i] + s[i+1:]):
                print(perm)
                out += [let+perm]
    return out

print(stringPermutation("abc"))