print("WERYFIKACJA PESELU")

a=int(input("Podaj swoj pesel:"))
plec=["kobieta","mezczyzna"]
while True:
    x=input("Podaj plec:")
    if(x in plec): break
y=input("Podaj rok urodzenia:")
z=int(input("Podaj który z koleji jest twój miesiac urodzenia w roku:"))

if z== 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    q=z%10
    print(q)




