#  Newton Raphson Method for solving equations
import sympy as sym


def func( x ):
    
	return x * x * x - x * x + 2

# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc( x ):
	return 3 * x * x - 2 * x

# Function to find the root
def newtonRaphson( x ):
	h = func(x) / derivFunc(x)
	while abs(h) >= 0.0001:
		h = func(x)/derivFunc(x)
		
		# x(i+1) = x(i) - f(x) / f'(x)
		x = x - h
	
	print("The value of the root is : ",
							"%.4f"% x)

# Driver program to test above
x0 = 1 # Initial values assumed
newtonRaphson(x0)

# x = sym.Symbol('x')
# function = x ** 4 + 7 * x ** 3 + 8
# derivitive = sym.diff(function)
# print(derivitive)