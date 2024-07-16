def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    '''
    Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
    '''
    if len(a[0]) != len(b):
        return -1
    
    result = []
    for row in a:
    
        # Compute the dot product of the current row and the vector 'b' and append the result to the result list
        dot_product = sum(row[i] * b[i] for i in range(len(b)))
        result.append(dot_product)
    
    return result