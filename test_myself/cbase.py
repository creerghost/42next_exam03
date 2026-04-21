def convert_base(n: str, b0: int, b1: int) -> str:
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    try:
        num = int(n, b0)
        if num == 0:
            return "0"
        while num:
            res += letters[num % b1]
            num //= b1
    except Exception:
        return "0"
    return res[::-1]

if __name__ == "__main__":
    print(convert_base("Ff", 16, 10))
    print(convert_base("00FF", 16, 2))
    print(convert_base("z", 36, 10))
    print(convert_base("0000", 7, 10))
    print(convert_base("0001", 2, 10))
    print(convert_base("1010", 2, 16))
    print(convert_base("133742", 8, 42))