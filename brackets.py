def bracket_validator(arg: str) -> bool:
    left = ['[', '{', '(']
    right = [']', '}', ')']
    res = []

    for b in arg:
        if b in left:
            res.append(b)
        elif b in right:
            if not res:
                return False
            t = res.pop()
            if b == ')' and t != '(':
                return False
            if b == '}' and t != '{':
                return False
            if b == ']' and t != '[':
                return False

    return len(res) == 0


if __name__ == "__main__":
    print(bracket_validator('([aa][]())'))
