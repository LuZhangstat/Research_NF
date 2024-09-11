Function Grad_Psi_a(x, a) 
Description: The derivative of psi_a(x) wrt a, (the first line in equation 11)
Input: x, a
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
