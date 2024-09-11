Function Grad_Psi_a(x, a) 
#Function Name: grad_psi_a_sparse
#grad_psi_a_sparse that calculates a sparse gradient vector from a given input vector x, using the value of its first element to determine the contents of the vector.
Description: The derivative of psi_a(x) wrt a, (the first line in equation 11)
Input: x, a
#A one-dimensional NumPy array representing the input vector.
#The elements of x are expected to be non-negative (x >= 0)
Output: V_a
V_a = (0)_n
If(x[i] > 0 for all i)
	If(x[1] \in (0, 1))
		V_a[1] = X[1]
	Else 
		V_a[1] = 1.0
	End if
End if
Return V_a
#Within Range (0, 1): If x[0] is between 0 and 1, but not including 1, the first component of the resulting sparse vector is set to x[0].
#Outside Range but Non-Negative: If x[0] is outside this range but still non-negative, the first component is set to 1.0.
#Negative Elements: If any element in x is negative, it returns an empty sparse vector of length n, indicating an undefined gradient under these conditions.
#The dimensions of this matrix are (n, 1) where n is the length of the input vector x.
