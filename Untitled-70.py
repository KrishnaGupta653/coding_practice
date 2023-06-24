d={'a':5,'b':6,'c':7}
d={key:value for (key,value) in d.items() if value is not None }
print(d)
