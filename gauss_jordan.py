import numpy as np

# Este esta basado y casi identico a un ejercicio en Matrix Computations de Golub, al final abandone
# mi idea por falta de tiempo.

def gauss_jordan(M):
    counter = 0
    row_count = len(M)
    column_count = len(M[0])
    
    for r in range(row_count):
        if counter >= column_count:
            return
        i = r
        while M[i][counter] == 0:
            i += 1
            if i == row_count:
                i = r
                counter += 1
                if column_count == counter:
                    return
                
        M[i],M[r] = M[r],M[i]
        lv = M[r][counter]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        
        for i in range(row_count):
            if i != r:
                lv = M[i][counter]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
                
        counter += 1
    return np.matrix(M)
 
 
matrix = [
   [ 1, 2, -1, -4],
   [ 2, 3, -1, -11],
   [-2, 0, -3, 22],]
 
print(gauss_jordan(matrix))



