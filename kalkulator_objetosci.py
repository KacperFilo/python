import math 

pole_p=["trojkat","czworobok","trapez","romb","rownoleglobok","szesciobok"]
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

if x=="stozek":
    r=int(input("Podaj krawedz r:"))
    H=int(input("Podaj wysokosc:"))
    d=(1/3)* (math.pi)  *r**2 *H
    print(d)


if x=="kula":
    r=int(input("Podaj krawedz r:"))
    d=(4/3)* (math.pi)  *r**3
    print(d)

if x=="ostroslup":
    H=int(input("Podaj wysokosc:"))
    while True:
        y=input("Podaj podstawe:")
        if(y in pole_p): break
    if y=="trojkat":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj bok a:"))
        Pp=a*h*(1/2)
        d=Pp*H*(1/3)
        print(d)
    if y=="czworobok":
        a=int(input("Podaj bok a:"))
        b=int(input("Podaj bok b:"))
        Pp=a*b
        d=Pp*H*(1/3)
        print(d)
    if y=="szesciobok":
        a=int(input("Podaj bok a:"))
        Pp=(3*a**2*math.sqrt(3))/2
        d=Pp*H*(1/3)
        print(d)
    if y=="romb":
        e=int(input("Podaj wysokosc trojkata:"))
        f=int(input("Podaj bok a:"))
        Pp=e*f*(1/2)
        d=Pp*H*(1/3)
        print(d)
    if y=="rownoleglobok":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj bok a:"))
        Pp=a*h
        d=Pp*H*(1/3)
        print(d)
    if y=="trapez":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj podstawe a:"))
        b=int(input("Podaj podstawe b:"))
        Pp=((a+b)*h)/2
        d=Pp*H*(1/3)
        print(d)


if x=="graniastoslup":
    H=int(input("Podaj wysokosc:"))
    while True:
        y=input("Podaj podstawe:")
        if(y in pole_p): break
    if y=="trojkat":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj bok a:"))
        Pp=a*h*(1/2)
        d=Pp*H
        print(d)
    if y=="czworobok":
        a=int(input("Podaj bok a:"))
        b=int(input("Podaj bok b:"))
        Pp=a*b
        d=Pp*H
        print(d)
    if y=="szesciobok":
        a=int(input("Podaj bok a:"))
        Pp=(3*a**2*math.sqrt(3))/2
        d=Pp*H
        print(d)
    if y=="romb":
        e=int(input("Podaj wysokosc trojkata:"))
        f=int(input("Podaj bok a:"))
        Pp=e*f*(1/2)
        d=Pp*H
        print(d)
    if y=="rownoleglobok":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj bok a:"))
        Pp=a*h
        d=Pp*H
        print(d)
    if y=="trapez":
        h=int(input("Podaj wysokosc trojkata:"))
        a=int(input("Podaj podstawe a:"))
        b=int(input("Podaj podstawe b:"))
        Pp=((a+b)*h)/2
        d=Pp*H
        print(d)
  
