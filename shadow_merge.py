def merge_list(l1: list[int], l2: list[int]) -> list[int]:
    return sorted(l1 + l2)


if __name__ == "__main__":
    print(merge_list([1, 3, 9], [2, 10, 8]))
