def shift_alpha(s: str, n: int) -> str:
    shifted = []

    for c in s:
        if 'a' <= c <= 'z':
            base = ord('a')
            shifted.append(chr(base + (ord(c) - base + n) % 26))
        elif 'A' <= c <= 'Z':
            base = ord('A')
            shifted.append(chr(base + (ord(c) - base + n) % 26))
        else:
            shifted.append(c)

    return ''.join(shifted)


if __name__ == "__main__":
    print(shift_alpha("abz", 1))
