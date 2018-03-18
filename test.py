import numpy as np

def echalonM(matrix):
    for i in range(min(len(matrix), len(matrix[0]))):
        for r in range(i, len(matrix)):
            zero_row = matrix[r][i] == 0
            if zero_row:
                continue
            
            matrix[i] = matrix[r]
            matrix[r] = matrix[i]

            first_row_col = matrix[i][i]

            for rr in range(i+1, len(matrix)):
                first_row = matrix[rr][i]
                multiple = -1 * first_row / first_row_col

                for cc in range(i, len(matrix[0])):
                    matrix[rr][cc] += matrix[i][cc] * multiple
            break

    result = ''
    for i in range(len(matrix)):
        result += str(matrix[i]) + '\n'
        
    return result

test_matrix = np.random.rand(5,5)

print(echalonM(test_matrix))

