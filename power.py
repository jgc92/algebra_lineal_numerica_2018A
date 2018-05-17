import numpy as np


def power_iteration(A, num_simulations):
    b_k = np.random.rand(A.shape[0])

    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)

        b_k1_norm = np.linalg.norm(b_k1,np.inf)

        b_k = b_k1 / b_k1_norm
        
        
        
        val = np.linalg.norm(np.dot(A,b_k), np.inf)
        v = (A - np.dot(val,np.eye(A.shape[0])))
        if np.allclose(, prev_x, rtol=1e-10):
            break
                        
    return val, b_k

sol = power_iteration(np.array([[2,1,1], [1, 2,1],[1,1,2]]), 1)


print(sol)
