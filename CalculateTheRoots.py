#This program calculates the roots of quadratic equation.

print("Calculate the roots of quadratic equations. a,b,c are numbers, not equal to zero.")

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))
x1 = ((-1*b)+(b*b - 4*a*c)**0.5)/(2*a)
x2 = ((-1*b)-(b*b - 4*a*c)**0.5)/(2*a) 
print("X1 = ",x1)
print("X2 = ",x2)