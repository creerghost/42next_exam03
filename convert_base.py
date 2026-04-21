def convert_base(n: str, base_n: int, base_res: int) -> str:
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if not (2 <= base_n <= 36 or 2 <= base_res <= 36):
            raise ValueError("huy")

        num = int(n, base_n)
        if num == 0:
            return "0"
        res = ""
        while num:
            res += letters[num % base_res]
            num //= base_res
        return res[::-1]
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    print(convert_base("Ff", 16, 10))
    print(convert_base("00FF", 16, 2))
    print(convert_base("z", 36, 10))
    print(convert_base("0000", 7, 10))
    print(convert_base("0001", 2, 10))
    print(convert_base("1010", 2, 16))
    print(convert_base("133742", 8, 42))
