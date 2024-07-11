def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 3)
print (result_1)
print (result_2)
print (result_3)
