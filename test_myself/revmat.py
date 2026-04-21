def revmat(mat):
    return [x[::-1] for x in mat]

print(revmat([[1, 2], [3, 4]]))