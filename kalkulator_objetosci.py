import math 

pole_p=["trojkat","czworobok","trapez","romb","rownoleglobok","szesciobok"]
bryla=["kula","stozek","walec","ostroslup","graniastoslup","prostopadloscian"]
while True:
    x=input("Podaj bryle:")
    if(x in bryla): break

if x=="prostopadloscian":
    while True:
        a=int(input("Podaj krawedz a:"))
        b=int(input("Podaj krawedz b:"))
        c=int(input("Podaj krawedz c:"))
        if(a and b and c > 0): break
    d=a*b*c
    print(d)

if x=="stozek":
    while True:
        r=int(input("Podaj krawedz r:"))
        H=int(input("Podaj wysokosc:"))
        if(r and H > 0): break
    d=(1/3)* (math.pi)  *r**2 *H
    print(d)


if x=="kula":
    while True:
        r=int(input("Podaj krawedz r:"))
        if(r  > 0): break
    d=(4/3)* (math.pi)  *r**3
    print(d)

if x=="ostroslup":
    while True:
        H=int(input("Podaj wysokosc:"))
        if(H > 0): break 
    while True:
        y=input("Podaj podstawe:")
        if(y in pole_p): break
    if y=="trojkat":
         while True:
                h=int(input("Podaj wysokosc trojkata:"))
                a=int(input("Podaj bok a:"))
                if(a and h > 0): break 
         Pp=a*h*(1/2)
         d=Pp*H*(1/3)
         print(d)
    if y=="czworobok":
         while True:
             a=int(input("Podaj bok a:"))
             b=int(input("Podaj bok b:"))
             if(a and b > 0): break
         Pp=a*b 
         d=Pp*H*(1/3)
         print(d)
    if y=="szesciobok":
         while True:
            a=int(input("Podaj bok a:"))
            if(a > 0): break
         Pp=(3*a**2*math.sqrt(3))/2
         d=Pp*H*(1/3)
         print(d)
    if y=="romb":
         while True:
             e=int(input("Podaj wysokosc trojkata:"))
             f=int(input("Podaj bok a:"))
             if(e and f > 0): break
         Pp=e*f*(1/2)
         d=Pp*H*(1/3)
         print(d)
    if y=="rownoleglobok":
         while True:
            h=int(input("Podaj wysokosc trojkata:"))
            a=int(input("Podaj bok a:"))
            if(a and h > 0): break
         Pp=a*h
         d=Pp*H*(1/3)
         print(d)
    if y=="trapez":
         while True:
            h=int(input("Podaj wysokosc trojkata:"))
            a=int(input("Podaj podstawe a:"))
            b=int(input("Podaj podstawe b:"))
            if(a and b and h > 0): break
         Pp=((a+b)*h)/2
         d=Pp*H*(1/3)
         print(d)


if x=="graniastoslup":
    while True:
        H=int(input("Podaj wysokosc:"))
        if(H > 0): break
    while True:
        y=input("Podaj podstawe:")
        if(y in pole_p): break
    if y=="trojkat":
        while True:
            h=int(input("Podaj wysokosc trojkata:"))
            a=int(input("Podaj bok a:"))
            if(a and h > 0): break
        Pp=a*h*(1/2)
        d=Pp*H
        print(d)
    if y=="czworobok":
        while True:
            a=int(input("Podaj bok a:"))
            b=int(input("Podaj bok b:"))
            if(a and b  > 0): break
        Pp=a*b
        d=Pp*H
        print(d)
    if y=="szesciobok":
        while True:
            a=int(input("Podaj bok a:"))
            if(a > 0): break
        Pp=(3*a**2*math.sqrt(3))/2
        d=Pp*H
        print(d)
    if y=="romb":
        while True:
            e=int(input("Podaj przekatna e:"))
            f=int(input("Podaj przekatna f:"))
            if(f and e > 0): break
        Pp=e*f*(1/2)
        d=Pp*H
        print(d)
    if y=="rownoleglobok":
        while True:
            h=int(input("Podaj wysokosc trojkata:"))
            a=int(input("Podaj bok a:"))
            if(a and h > 0): break
        Pp=a*h
        d=Pp*H
        print(d)
    if y=="trapez":
        while True:
            h=int(input("Podaj wysokosc trojkata:"))
            a=int(input("Podaj podstawe a:"))
            b=int(input("Podaj podstawe b:"))
            if(a and b and h > 0): break
        Pp=((a+b)*h)/2
        d=Pp*H
        print(d)
  
