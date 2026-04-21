def vovel(s: str) -> int:
    vvl = "aeiou"
    cnt = 0
    for c in s:
        if c in vvl:
            cnt += 1
    return cnt


def sorter(lst: list[str]) -> list[str]:
    vvl = "aeiou"
    lst_v = []
    for str in lst:
        lst_v.append(len([x for x in str if x in vvl]))
    if not all(x == lst_v[0] for x in lst_v):
        return sorted(lst, key=vovel)
    if not all(len(w) == len(lst[0]) for w in lst):
        return sorted(lst, key=len)
    return sorted(lst)

print(sorter(["Apple", "banana", "Kiwi", "grape"]))
print(sorter(["dog", "cat", "hi", "a"]))