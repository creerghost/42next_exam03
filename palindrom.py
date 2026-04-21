def palindrome(arg: str) -> bool:
    return (arg == arg[::-1])


if __name__ == "__main__":
    print(palindrome("madam"))
