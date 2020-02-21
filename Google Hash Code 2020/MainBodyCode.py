def Conversion(OLDFILE, NEWFILE):
    for i in OLDFILE:
        i = int(i)
        NEWFILE.append(i)
    OLDFILE = []


A = []
B = []
C = []
D = []
E = []
G = []
H = []
F = []
K = []
c = []
M = []
P = {}

X = input().split(" ")
Y = input().split(" ")
Conversion(X, A)
Conversion(Y, B)

for i in range(A[1]):
    E = []
    D = []
    C = []
    Z = input().split(" ")
    W = input().split(" ")
    Conversion(Z, C)
    Conversion(W, D)
    sum = 0
    G.append(i)
    for j in D:
        sum += B[j]
    G.append(sum)
    K.append(sum)
    G.append(C)
    G.append(D)
    F.append(G)
    G = []

for j in range(len(F)):
    for i in F:
        b = 0
        a = i[1]
        if (a > b):
            b = a
            c = (i[3])
            d = i
        else:
            pass
    M.append(i[0])
    H.append(c)

    del F[F.index(i)]

print(len(M))
for i in M:
    print(i, end=" ")
    k = M.index(i)
    r = H[k]
    print(len(r))
    for j in r:
        print(j, end=" ")
    print("")
