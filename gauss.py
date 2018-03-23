def gauss(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   for i in range(k,n):
     print(M[k][k])
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass

   # Show the matrix
   for row in M:
     print(row)
   print()

   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]
          
   # Show the matrix
   for row in M:
     print(row)
   print()


  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  print(x)


  

A = [[0.03, 58.9], [5.31, -6.10]]
b = [59.2, 47.0]

gauss(A,b)
