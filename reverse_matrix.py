def reverse_matrix(arg: list[list[int]]) -> list[list[int]]:
    return [x[::-1] for x in arg]


if __name__ == "__main__":
    print(reverse_matrix([[1, 2], [3, 4]]))
