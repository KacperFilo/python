


a=int(input("Podaj liczbe a:"))

b=int(input("Podaj liczbe b:"))

dzialanie=["dodawanie","odejmowanie","iloczyn","iloraz","potegowanie","modulo"]
while True:
    c=input("Podaj dzialanie:")
    if(c in dzialanie): break

if c=="dodawanie":
    d=a+b
    print(d)

if (c=="odejmowanie"):
    d=a-b
    print(d)


if (c=="mnozenie"):
    d=a*b
    print(d)

if (c=="dzielenie"):
    if b==0:
        print("Blad")
    else:
        d=a/b
    print(d)
       

if (c=="potegowanie"):
    d=a**b
    print(d)

if (c=="modulo"):
    if b==0:
        print("Blad")
    else:
        d=a%b
    print(d)

