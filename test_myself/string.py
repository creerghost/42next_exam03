def string(s: str):
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    flag = True
    res = ""
    for c in s:
        if c.isalpha() and flag:
            res += c.lower()
            flag = not flag
        elif c.isalpha() and not flag:
            res += c.upper()
            flag = not flag
        else:
            res += c
    return res

print(string("Hello !World!"))