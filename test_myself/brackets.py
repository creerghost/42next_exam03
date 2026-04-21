def brackets(arg: str) -> bool:
    tmp = []
    ll = ['[', '{', '(']
    rr = [']', '}', ')']
    for c in arg:
        if c in ll:
            tmp.append(c)
        elif c in rr:
            if not tmp:
                return False
            tmpp = tmp.pop()
            if c == ')' and tmpp != '(':
                return False
            if c == '}' and tmpp != '{':
                return False
            if c == ']' and tmpp != '[':
                return False
    return len(tmp) == 0


print(brackets('([aa][]())'))