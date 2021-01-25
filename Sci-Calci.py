# Functions for the program
class Series:
    private:

    public:
        def Arithmetic(self, a, d, flag=0):
            n = int(input("Enter total no of terms: "))
            if flag == 0:
                if n <= 0:
                    print(f"\n{n}th term of A.P does not exist.")
                    print("\nSum of A.P = 0  (Since, no terms to compute sum)")
                elif n >= 1:
                    tn = a + (n - 1) * d
                    print(f"{n}th term of the A.P= {tn}\r")
                    Sum = n * ((a + tn) / 2)
                    print(f"Sum of A.P = {Sum}")
                    # print(f"A.M = {Sum/n}")
            elif flag == 1:
                if n <= 0:
                    print(f"\n{n}th term of H.P does not exist.")
                    print("\nSum of H.P = 0  (Since, no terms to compute sum)")
                elif n >= 1:
                    tn = a + (n - 1) * d
                    print(f"{n}th term of the H.P= {1/tn}\r")
                    Sum = n * ((a[0] + tn) / 2)
                    print(f"Sum of H.P = {Sum}")
                    # print(f"H.M = {Sum/n}")


        def Geometric(self, a, r):
            n = int(input("Enter total no of terms: "))
            if n <= 0:
                print("\nSum of the sequence = 0 \t Since, there are no terms to compute sum. ")
                print(f"\n{n}th term of the G.P does not exist.")
            elif n >= 1:
                tn = a * pow(r, n - 1)
                print(f"{n}th term of the G.P= {tn}\r")
                if r < 1:
                    if n < 20:
                        Sum = (a * (1 - pow(r, n))) / (1 - r)
                        print(f"Sum of G.P = {Sum}")
                    elif n >= 20:
                        Sum = a / (1 - r)
                        print(f"Sum of G.P = {Sum}")
                elif r > 1:
                    if n <= 50:
                        Sum = (a * (1 - pow(r, n))) / (r - 1)
                        print(f"Sum of G.P = {Sum}")
                    else:
                        print("Sum of G.P= Infinity")
                elif r == 1:
                    Sum = n * a
                    print(f"Sum of G.P = {Sum}")
                    exit()


        def AGP(self, a, diff, r):
            n = int(input("Enter total no of terms: "))
            if n >= 1:
                tn = (a + (n - 1) * diff) * pow(r, n - 1)
                print(f"\n{n}th term of the sequence= {tn}")
                if r < 1:
                    Sum = a / (1 - r) + (diff * r(1 - pow(r, n - 1)) / pow((1 - r), 2))
                    print(f"\nSum of the sequence= {Sum}")
            elif n <= 0:
                print("\nSum of the sequence = 0 \t Sine, there are no terms to compute sum. ")
                print(f"\n{n}th term of the sequence does not exist.")


class Arithmetic:
    private:

    public:
        def add(a, b):
            return  a + b


        def subtract(a, b):
            return  a - b


        def multiply(a, b):
            return a * b


        def division(a, b):
            return a / b


        def power(a, n):
            return pow(a, n)



class Matrix:
    private:

    public:
        @staticmethod
        def show(mat, row, col):
            for r in range(0, row):
                for c in range(0, col):
                    print(mat[r][c], end=' ')
                print("\r")


        @staticmethod
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


        @staticmethod
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


        @staticmethod
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


        @staticmethod
        def matrixMultiply(matrix_a, matrix_b, row_a, col_a, col_b):
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


        def coFactor(self):


        def determinant(self, matrixA, row, col):

