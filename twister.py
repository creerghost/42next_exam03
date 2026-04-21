def twister(lst: list[int], s: int) -> list[int]:
    for _ in lst:
        tmp = lst.pop()
        lst.insert(0, tmp)
        s -= 1
        if s == 0:
            break
    return lst


if __name__ == "__main__":
    print(twister([1, 2, 3, 4, 5], 2))
    print(twister([4, 2, 1, -1, 'a'], 4))
    print(twister([], 3))
    print(twister([1], 10))
