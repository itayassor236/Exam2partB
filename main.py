
def nevile(table, point):
    myarr=[[0 for col in range(len(table))]for row in range(len(table))]
    for i in range(len(table)):
        if i==0:
            for j in range(len(table)):
                myarr[j][j]=table[j][1]
        else:
            for k in range(len(table)):
                if k+i<len(table):
                 myarr[k][k+i]=(((point-table[k][0])*myarr[k+1][k+i])-((point-table[k+i][0])*myarr[k][k+i-1]))/(table[k+i][0]-table[k][0])
                 print("p", i, j, "=", myarr[i][j])
    print("The value of f(", point, ") is :",round(myarr[0][len(table)-1],5) )


def polynom(table, point):
    if len(table) < 3:
        print("cant calculate")
    else:
        i = 0
        mat = [[1], [1], [1]]
        vec = [[], [], []]

        while table[i][0] < point and table[i + 1][0] < point and table[i + 2][0] < point:
            i += 1
        mat[0].append(table[i][0])
        mat[0].append((table[i][0]) ** 2)
        mat[1].append(table[i + 1][0])
        mat[1].append((table[i + 1][0]) ** 2)
        mat[2].append(table[i + 2][0])
        mat[2].append((table[i + 2][0]) ** 2)
        vec[0].append(table[i][1])
        vec[1].append(table[i + 1][1])
        vec[2].append(table[i + 2][1])
        """""
        a=choice(table)
        if a==table[len(table)-2] or a==table[len(table)-1]:
            a=table[len(table)-3]
        mat[0].append(a[0])
        mat[0].append(a[0]**2)
        vec[0].append(a[1])
        b=a
        while b==a or (b[0]<a[0]):
            b=choice(table)
        if b==table[len(table)-1]:
            b=table[len(table)-2]
        mat[1].append(b[0])
        mat[1].append(b[0] ** 2)
        vec[1].append(b[1])
        c=a
        while (c==a or c==b) or c[0]<b[0]:
            c=choice(table)
        mat[2].append(c[0])
        mat[2].append(c[0] ** 2)
        vec[2].append(c[1])

        #mat=[[1,1,1],[1,2,4],[1,3,9]]
        vec=[[0.8415],[0.9093],[0.1411]]
        mat=getMatrixInverse(mat)

        mat = [[1, 2, 4], [1, 3, 9], [1, 4, 16]]
        vec = [[0.9093], [0.1411],[-0.7568]]
        """""
        mat = getMatrixInverse(mat)
        g = mult(mat, vec)
        sum = g[0][0] + (g[1][0] * point) + (g[2][0] * (point ** 2))
        print("the point of", point, "is", round(sum, 5))

def transposeMatrix(m):
    a= list(map(list,zip(*m)))
    return a

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = round(getMatrixDeternminant(m),6)
    if len(m) == 2:
        return [[round(m[1][1]/determinant,6), round(-1*(m[0][1]/determinant),6)],
                [round(-1*(m[1][0]/determinant),6), round(m[0][0]/determinant,6)]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def mult(matrix1,matrix2):
    res=[[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    size=len(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


itayID=[3,1,8,2,3,1,9,2,5]
question2=itayID[8]
print("The question selected is :",question2)
table=[[1.2,3.5095],[1.3,3.6984],[1.4,3.9043],[1.5,4.1293],[1.6,4.3756]]
point=1.37
nevile(table,point)
polynom(table,point)