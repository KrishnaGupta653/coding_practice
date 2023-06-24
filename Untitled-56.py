n="racecar"
c=0
for i in range(0,len(n)):
    print(">",n[-i-1])
    if n[i]==n[-i-1]:
        c+=1
if c>=1:
    print("palindrome")
print(c)