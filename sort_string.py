def count_vowels(word: str) -> int:
    vowels = "aeiou"
    res = 0
    for v in word:
        if v in vowels:
            res += 1
    return res


def sort_string(args: list[str]) -> list[str]:
    vovels = "aeiou"
    lens_v = []
    for string in args:
        lens_v.append(len([x for x in string if x in vovels]))
    if not all(x == lens_v[0] for x in lens_v):
        print("sort by vowels")
        return sorted(args, key=count_vowels)
    if not all(len(x) == len(args[0]) for x in args):
        print("sort by len")
        return sorted(args, key=len)
    print("sort by alphabet")
    return sorted(args)


if __name__ == "__main__":
    while True:
        try:
            i = input("write string: ")
            print()
            print(sort_string(i.split(" ")))
            print()
        except KeyboardInterrupt:
            print("\nbye!")
            break
