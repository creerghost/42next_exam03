def pat(s):
    res = 0
    nums = "0123456789"
    for i in range(0, len(s) - 1, 1):
        if s[i] in nums:
            if s[i + 1] in nums:
                if int(s[i]) < int(s[i+1]):
                    res += 1
    return res
print(pat("123a345"))