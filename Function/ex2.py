def ChangeMatrix():
    ''' hàm chuyển vị ma trận this function is change póition of matrix'''
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            print(matrix[row][col], end=" ")
        print()
ChangeMatrix()
