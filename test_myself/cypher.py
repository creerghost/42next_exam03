def cyp(s: str, n: int):
    res = []
    
    for c in s:
        if 'a' <= c <= 'z':
            base = ord('a')
            res.append(chr(base + (ord(c) - base + n) % 26))
        elif 'A' <= c <= 'Z':
            base = ord('A')
            res.append(chr(base + (ord(c) - base + n) % 26))
        else:
            res.append(c)
    return ''.join(res)

print(cyp("abz", 1))