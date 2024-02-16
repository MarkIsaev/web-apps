def matrix_multiplication(n, matrix_A, matrix_B):
    result_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result_matrix

if __name__ == "__main__":
    n = int(input())
    matrix_A = []
    matrix_B = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_A.append(row)

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix_B.append(row)

    result_matrix = matrix_multiplication(n, matrix_A, matrix_B)

    for row in result_matrix:
        print(*row)