k=0
for i in range(1,6):
    k=k+1
    for j in range(0,i+1):
      if(i==1 and j==0):
        print("*",end=" ")
      elif(j==0 or j==k or i==5):
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()
