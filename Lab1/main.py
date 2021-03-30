fin = open("input.txt")
fout = open("output.txt", "w")
a, b = map(float, fin.readline().split())

nA, mA = map(int, fin.readline().split())
A = []
for i in range(nA):
    A.append([0] * mA)
x = fin.readline().split()
k = 0
for i in range(nA):
    for j in range(mA):
        A[i][j] = float(x[k])
        k = k + 1

nB, mB = map(int, fin.readline().split())
B = []
for i in range(nB):
    B.append([0] * mB)
x = fin.readline().split()
k = 0
for i in range(nB):
    for j in range(mB):
        B[i][j] = float(x[k])
        k = k + 1

nC, mC = map(int, fin.readline().split())
C = []
for i in range(nC):
    C.append([0] * mC)
x = fin.readline().split()
k = 0
for i in range(nC):
    for j in range(mC):
        C[i][j] = float(x[k])
        k = k + 1

nD, mD = map(int, fin.readline().split())
D = []
for i in range(nD):
    D.append([0] * mD)
x = fin.readline().split()
k = 0
for i in range(nD):
    for j in range(mD):
        D[i][j] = float(x[k])
        k = k + 1

nF, mF = map(int, fin.readline().split())
F = []
for i in range(nF):
    F.append([0] * mF)
x = fin.readline().split()
k = 0
for i in range(nF):
    for j in range(mF):
        F[i][j] = float(x[k])
        k = k + 1

BT = []
for i in range(mB):
    BT.append([0] * nB)
for i in range(mB):
    for j in range(nB):
        BT[i][j] = b * B[j][i]

for i in range(nA):
    for j in range(mA):
        A[i][j] = a * A[i][j]

if (mB != nA or nB != mA):
    print(0, file=fout)
    exit(0)
for i in range(nA):
    for j in range(mA):
        A[i][j] = A[i][j] + BT[i][j]

AT = []
for i in range(mA):
    AT.append([0] * nA)
for i in range(mA):
    for j in range(nA):
        AT[i][j] = A[j][i]

if (mC != mA):
    print(0, file=fout)
    exit(0)

Anew = []
for i in range(nC):
    Anew.append([0] * nA)
for i in range(nC):
    for j in range(nA):
        for k in range(mC):
            Anew[i][j] = Anew[i][j] + C[i][k] * AT[k][j]
if (nA != nD):
    print(0, file=fout)
    exit(0)

new = []
for i in range(nC):
    new.append([0] * mD)
for i in range(nC):
    for j in range(mD):
        for k in range(nD):
            new[i][j] = new[i][j] + Anew[i][k] * D[k][j]
if (nC != nF or mD != mF):
    print(0, file=fout)
    exit(0)

for i in range(nC):
    for j in range(mD):
        new[i][j] = new[i][j] - F[i][j]
print(1, file=fout)
print(nF, file=fout, end=" ")
print(mF, file=fout)
for i in range(nC):
    for j in range(mD):
        print(new[i][j], file=fout, end=" ")

fout.close()
