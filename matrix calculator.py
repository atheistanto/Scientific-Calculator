from typing import List


def inverse(matrix):
    return Adj(matrix)/determinant(matrix, 3)


def coFactor(mat, k, h):
    if len(mat) == 3:
        matrix = []
        temp = []
        for row in range(3):
            for col in range(3):
                if row == k or col == h:
                    continue
                else:
                    temp.append(mat[row][col])
            matrix.append(temp)
            temp.clear()
        det = determinant(matrix, 2)
        if (row + col) % 2 == 0:
            factor = 1
        elif (row + col) % 2 != 0:
            factor = -1
        return factor * det
    elif len(mat) == 2:
        for row in range(2):
            for col in range(2):
                if row != k and col != h:
                    if (row+col)%2 == 0:
                        return mat[row][col]
                    elif (row+col)%2 == 1:
                        return -1*mat[row][col]


def determinant(mat, order):
    det = 0
    if order == 2:
        det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][1]
    elif order == 3:
        det = mat[0][0] * coFactor(mat, 0, 0) + mat[0][1] * coFactor(mat, 0, 1) + mat[0][2] * coFactor(mat, 0, 2)
    return det


def Adj(mat):
    if len(mat) == 3:
        adjMat = []
        temp = []
        for row in range(3):
            for col in range(3):
                temp.append(coFactor(mat[row][col]))
            adjMat.append(temp)
            temp.clear()


def show(mat, row, col):
    for r in range(0, row):
        for c in range(0, col):
            print(mat[r][c], end=' ')
        print("\r")


def matrixAdd(matA, matB, row, col):
    matC = []
    for x in range(row):
        res = []
        for y in range(col):
            res.append(matA[x][y] + matB[x][y])
        matC.append(res)
    print("Addition of the two matrices= \r")
    # print(matC)
    return matC


def subtract(matA, matB, row, col):
    matC = []
    for x in range(row):
        res = []
        for y in range(col):
            res.append(matA[x][y] - matB[x][y])
        matC.append(res)
    print("Subtraction of the two matrices(matrix1 - matrix2)= \r")
    # print(matC)
    return matC


def transpose(mat):
    transpose_mat = []
    x = 0
    y = 0
    for x in range(len(mat[0])):
        dummy = []
        for y in range(len(mat)):
            dummy.append(mat[y][x])
        transpose_mat.append(dummy)
    return transpose_mat


def mat_multiplication(matrix_a, matrix_b, row_a, col_a, col_b):
    matrixC = []
    dummy = []
    for k in range(0, row_a):
        dummy = []
        for x in range(0, col_b):
            temp = 0
            for y in range(0, col_a):
                temp += matrix_a[k][y] * matrix_b[y][x]
                # print(f"temp{[x]}{[y]}= {temp}", end='\t')
            # print("\r")
            dummy.append(temp)
        matrixC.append(dummy)
    print("The multiplication of matrix1 and matrix2= \r")
    return matrixC


def main():
    while True:
        print("Choose the matrix operation:\r1. add\t4. multiply\r2. subtract\t5. determinant\r3. transpose\t6.inverse")
        my_str = input("Enter your choice: ")

        if my_str.lower() == 'add' or my_str.lower() == 'addition' or my_str.lower() == '1':
            matrixA = []
            matrixB = []
            resultant_matrix = []
            Row = int(input("Enter no. of rows: "))
            Col = int(input("Enter no. of columns: "))

            for i in range(0, Row):
                a = []
                for j in range(0, Col):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixA.append(a)

            for i in range(0, Row):
                a = []
                for j in range(0, Col):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixB.append(a)

            print("Your entered elements for matrix1 in matrix form: \r")
            show(matrixA, Row, Col)
            print("Your entered elements for matrix2 in matrix form: \r")
            show(matrixB, Row, Col)
            print("\r")

            resultant_matrix = matrixAdd(matrixA, matrixB, Row, Col)
            show(resultant_matrix, Row, Col)

        elif my_str.lower() == 'subtract' or my_str.lower() == 'sub' or my_str.lower() == '2':
            matrixA = []
            matrixB = []
            resultant_matrix = []
            Row = int(input("Enter no. of rows: "))
            Col = int(input("Enter no. of columns: "))

            for i in range(0, Row):
                a = []
                for j in range(0, Col):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixA.append(a)

            for i in range(0, Row):
                a = []
                for j in range(0, Col):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixB.append(a)

            print("Your entered elements for matrix1 in matrix form: \r")
            show(matrixA, Row, Col)

            print("Your entered elements for matrix2 in matrix form: \r")
            show(matrixB, Row, Col)
            print("\r")

            resultant_matrix = subtract(matrixA, matrixB, Row, Col)
            show(resultant_matrix, Row, Col)

        elif my_str.lower() == 'transpose' or my_str.lower() == 'trans' or my_str.lower() == '3':
            matrix = []
            result = []
            Row = int(input("Enter no. of rows: "))
            Col = int(input("Enter no. of cols: "))

            for i in range(0, Row):
                a = []
                for j in range(0, Col):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrix.append(a)

            print("Your elements in matrix form: \r")
            show(matrix, Row, Col)

            print("The transpose of the entered matrix: \r")
            result = transpose(matrix)
            show(result, Col, Row)

        elif my_str.lower() == 'multiplication' or my_str.lower() == 'multiply' or my_str.lower() == '4':
            matrixA = []
            matrixB = []
            result = []
            RowA = int(input("Enter no. of rows in matrix 1: "))
            ColA = int(input("Enter no. of columns in matrix1 : "))
            RowB = ColA
            print("For matrix multiplication, the no. of rows of matrix1 is equal to the no of colums of matrix2.\r")
            ColB = int(input("Enter no. of columns in matrix2: "))

            for i in range(0, RowA):
                a = []
                for j in range(0, ColA):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixA.append(a)

            for i in range(0, RowB):
                a = []
                for j in range(0, ColB):
                    a.append(int(input(f"Enter {(i + 1), (j + 1)}th element: ")))
                matrixB.append(a)

            print("Your elements for matrix 1 in matrix form: \r")
            show(matrixA, RowA, ColA)
            print("Your elements for matrix 2 in matrix form: \r")
            show(matrixB, RowB, ColB)
            print("The multiplication of matrix1 and matrix2= \r")
            resultant_matrix = mat_multiplication(matrixA, matrixB, RowA, ColA, ColB)
            show(resultant_matrix, RowA, ColB)
        else:
            print("\r Your choice is invalid")

        choice = input("\n\n\nPress X to terminate this program")
        if choice.upper() == 'X':
            exit()
        else:
            continue


main()