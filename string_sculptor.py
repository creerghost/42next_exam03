def sculptor(arg: str) -> str:
    res = ""
    flag = True
    for i in range(0, len(arg), 1):
        if arg[i].isalpha() and flag:
            res += arg[i].lower()
            flag = not flag
        elif arg[i].isalpha() and not flag:
            res += arg[i].upper()
            flag = not flag
        else:
            res += arg[i]
    return res


if __name__ == "__main__":
    print(sculptor("a-bC-dEf-ghIj"))
