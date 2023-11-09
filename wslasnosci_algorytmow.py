
import time







#n=int(input("Podaj liczbe calkowita:"))
#suma=0
#i=1
#while i<=n:
#    suma+=i
#    i+=1
#print(suma)

"""x=int(input("Podaj wartosc dodatia:"))
if x%2==0:
    print(x/2)
else:
    j=0
    suma2=0

    while j<x:
        suma2=suma2+2*j
        j+=1
    print(suma2)"""

# Notacja O()

# O(1)

# O(n)

# O(n^2)
#lista=[1,2,3,4,5,6,7,8,9,10]
#for i in lista:
#    print(i)

"""def lin_search(lst, val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i 
        
lst=[1,2,3,4,5,6,7,8,9,10]
print(lin_search(lst, 9))"""

start=time.time()

n=int(input("Podaj licze calkowita: "))
for i in range(n):
    for j in range(n):
        print("#",end='')
print()

end=time.time()

print(end-start)



