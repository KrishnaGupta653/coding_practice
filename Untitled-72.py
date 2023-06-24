d={'a':5,'b':6,'c':7}
d['d']=4
for i in d:
    print(i)
for i in d.keys():
    print(i)

for i in d.values():
    print(i)
print(d.values())
print(d.items())
for i in enumerate(d.items()):
    print(i)
for i,j in d.items():
    print(i,j)
for i in d.items():
    print(i)
print(d.get('a'))
print(d)
for i in reversed(d.items()):
    print(i)