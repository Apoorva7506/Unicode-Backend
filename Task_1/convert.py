str=input("Please enter binary numbers separated by a ',' \n")
l=str.split(',')

j=[]
for i in l:
    t=int(i,2)
    if t%5==0:
        j.append(i)
print (j)