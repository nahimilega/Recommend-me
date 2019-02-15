import numpy as np
 
 
 

def matrix_factorization(full_matrix, P, Q, K, iteration=16000, alpha=0.0015, beta=0.01):
    '''
    This function uses gradient desent technique to fill the empty boxes in full user rating matrix
    and breaks the matrises into two different matrix P and Q
    full_matrix=P*Qtranspose
    Paremeters-

    '''
    Q = Q.T
    for iterate in range(iteration):
        for i in range(len(full_matrix)):
            for j in range(len(full_matrix[i])):
                
                if full_matrix[i][j] > 0:
                    
                    eij = full_matrix[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])


        eR = np.dot(P,Q)
        e = 0
        for i in range(len(full_matrix)):
            for j in range(len(full_matrix[i])):
                
                if full_matrix[i][j] > 0:
                    e = e + pow(full_matrix[i][j] - np.dot(P[i,:],Q[:,j]), 2)   #TO find rms error
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        
        if (iterate+1) % 10 == 0:                     #This will display after 10 itrations
                print("Iteration: " + str(iteration) +"error "+ str(e)))
        if e < 0.001:
            break
    full_matrix=numpy.matmul(P,Q.T)        
    return (P, Q.T,full_matrix)

###############################################################################

if __name__ == "__main__":
    f = open("user_rating_matrix.txt", "r")
    final_matrix=[]
    for x in f:
        if(x!='\n'):
            new=list(map(float,x.split(',')))
            
            final_matrix.append(new)

        
    

    full_matrix = np.array(final_matrix)

    N = len(full_matrix)
    M = len(full_matrix[0])
    K = 10

    P = np.random.rand(N,K)
    Q = np.random.rand(M,K)

    nP, nQ ,full_final_matrix= matrix_factorization(full_matrix, P, Q, K)

    with open('p_value.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(nP)
    writeFile.close()    

    with open('q_value.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(nQ)
    writeFile.close() 

    with open('full_matrix_value.txt', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(full_final_matrix)
    writeFile.close()