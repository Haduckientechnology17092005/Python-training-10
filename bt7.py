def longest_common_subsquence(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0]*(n+1) for i in range(m+1)]
    longest = 0
    max_index = 0
    for i in range (1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                if L[i][j] > longest:
                    longest = L[i][j]
                    max_index = i
            else:
                L[i][j] = 0
    start_index = max_index - longest
    return X[start_index:max_index]

X = input("nhap xau 1: ")
Y = input("nhap xau 2: ")

print(longest_common_subsquence(X, Y))