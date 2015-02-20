__author__ = 'Ramon'


#running time = O(n^2)
def sum_matrix(X, Y):
    i, j = 0, 0
    Z = []
    result = []

    while i < len(X):
        while j < len(X[0]):
            Z.append(X[i][j] + Y[i][j])
            j += 1
        i += 1
        j = 0
        result.append(Z)
        Z = []
    return result


#running time = O(n^3)
def mul_straightforward(X, Y):
    i, j, k = 0, 0, 0
    Z, result = [], []
    sum1 = 0
    n = len(X)

    while i < n:
        while j < n:
            while k < n:
                sum1 += X[i][k] * Y[k][j]
                k += 1
            j += 1
            k = 0
            Z.append(sum1)
            sum1 = 0
        j = 0
        i += 1
        result.append(Z)
        Z = []

    return result


# Idea: Multiply 2 matrices (n x n) (X and Y) using 8 recursive calls with divide and conquer
def divide_and_conquer_matrix_mul(X, Y):
    #base case
    if len(X) == 2:
        print("Base case")
        print("X=", X, "Y=", Y)
        D = [[(X[0][0]*Y[0][0]+X[0][1]*Y[1][0]), (X[0][0]*Y[0][1]+X[0][1]*Y[1][1])],
            [(X[1][0]*Y[0][0]+X[1][1]*Y[1][0]), (X[1][0]*Y[0][1]+X[1][1]*Y[1][1])]]
        return D
    else:
        n_middle = int(len(X)/2)
        A = divide_and_conquer_matrix_mul(X[:n_middle], Y[:n_middle])
        B = divide_and_conquer_matrix_mul(X[n_middle:], Y[n_middle:])
        C = A + B
        return C


# Idea: Multiply 2 matrices (n x n) (X and Y) using only 7 recursive calls (instead of 8)
def strassen(X, Y):
    #base case
    if len(X) == 1 and len(Y) == 1:
        return X


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("A=", A, "with len(A[0])=", len(A[0]), "and len(A)=", len(A))
    B = A[:int(len(A)/2)]
    print("B=", B, "with len(B[0])=", len(B[0]), "and len(B)=", len(B))
    C = A[int(len(A[0])/2):]
    print("C=", C, "with len(C[0])=", len(C[0]), "and len(C)=", len(C))
    D = B[0]
    print("D=", D, "and len(D)=", len(D))

    print("A + A=", sum_matrix(A, A))

    F = [[1, 2], [3, 4]]
    print("F * F=", mul_straightforward(F, F))

    G = [[(F[0][0]*F[0][0]+F[0][1]*F[1][0]), (F[0][0]*F[0][1]+F[0][1]*F[1][1])],
        [(F[1][0]*F[0][0]+F[1][1]*F[1][0]), (F[1][0]*F[0][1]+F[1][1]*F[1][1])]]
    print("G = F * F=", G)

    H = [[1, 2, 3, 4], [3, 4, 3, 4], [5, 6, 3, 4], [7, 8, 3, 4]]
    HL = H[:int(len(H)/2)]
    HR = H[int(len(H)/2):]
    print("HL=", HL, "and HR=", HR)

    I = HL + HR
    print("I=", I)

    print("F * F=", divide_and_conquer_matrix_mul(H, H))