import math 


bryla=["kula","stozek","walec","ostroslup","graniastoslup","prostopadloscian"]
while True:
    x=input("Podaj bryle:")
    if(x in bryla): break

if x=="prostopadloscian":
    a=int(input("Podaj krawedz a:"))
    b=int(input("Podaj krawedz b:"))
    c=int(input("Podaj krawedz c:"))
    d=a*b*c
    print(d)

if x=="kula":
    r=int(input("Podaj krawedz r:"))
    d=(4/3)* (math.pi)  *r**3
    print(d)
