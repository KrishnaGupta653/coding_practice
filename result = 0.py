result = 0.0
sign= 1.0
fact =1.0
n=5
x=0.52
for i in range(1, n+1, 2): 
    term = sign*pow(x,i)/fact
    result += term
    sign*=-1
    fact*= (i+1)*(i+2) 

print(result)