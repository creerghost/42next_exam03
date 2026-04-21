def pattern_tracker(arg: str) -> int:
    count = 0
    nbrs = "0123456789"
    # for i, c in enumerate(arg):
    #     if c[i] in nbrs:
    #         if c[i + 1] in nbrs:
    #             if int(c[i]) < int(c[i + 1]):
    #                 count += 1
    for i in range(0, len(arg) - 1, 1):
        if arg[i] in nbrs:
            if arg[i + 1] in nbrs:
                if int(arg[i]) < int(arg[i + 1]):
                    count += 1
    return count


if __name__ == "__main__":
    print(pattern_tracker("012345"))
