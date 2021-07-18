S = [3, 1, 3, 1]
N = len(S)-1
big_val = 1 << 62 # left bitwise shift is equivalent to raising 2 to the power of the positions shifted. so, big_val = 2 ^ 62.
A = [[big_val for i in range(N+1)] for j in range(N+1)]


def matrix_chain_cost(i, j):
    global A 
    if i == j: 
        return 0
    if A[i][j] != big_val:
        return A[i][j]

    for k in range(i, j):    
        A[i][j] = min(A[i][j], matrix_chain_cost(i, k) + matrix_chain_cost(k+1, j) + S[i-1] * S[k] * S[j])

    return A[i][j]



print("Minimum cost of multiplication is", matrix_chain_cost(1, N))