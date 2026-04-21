def twist(lst: list[int], n):
    for _ in lst:
        tmp = lst.pop()
        lst.insert(0, tmp)
        n -= 1
        if n == 0:
            break
    return lst

print(twist([1, 2, 3, 4, 5], 2))