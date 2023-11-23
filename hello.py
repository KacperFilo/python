import math
import random
print("Hello world")
#kometarz

a=121
b=10.5

print(a)
print('%.20f'%b)

tekst1='ala ma kota'
tekst2="Ala ma kota"

print("Wartosc zmiennej a wynosi: ",a)
print(" Wartosc zmiennej a wynosi: %.2f" %a)

print(" Wartosc zmiennej a wynosi:"+str (a))

# imie=input()
# print("Czesc,",imie)

# wiek=int(input("Ile masz lat?"))
# print(wiek)

# suma=1+1
# roznica=2-1
# iloczyn=3*8
# iloraz=6/3
# modulo=4%2
# potega=2**3

# potega2=math.pow()
# los=random.randint()
# print(los)

# if a >0:
#     print("Liczba a wieksza od 0")
# elif a==0:
#     print("Liczba jest rowna 0")
# else:
#     print("LIczba jest mniejsza lub rowna 0")


# if a%2==0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba jest nieparzysta")

# for i in range(3):
#     print(i+1)

# for i in range(1, 100):
#     print(i)

# for i in range(1, 100, 2):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# for i in range(1,100):
#     print (i)
#     if a%2==0:
#         print("Liczba jest parzysta")
#     else:
#         print("Liczba jest nieparzysta")


# for i in range(6):
#     print(random.randint(1, 100))


# for i in "string":
#     if i=="r":
#         break
#     print(i)

# for i in "string":
#     if i=="r":
#         continue
#     print(i)

# while a>0:
#     print(f"liczba {a}jest wieksza od 0")
#     a-=1

# while True:
#     print("To zawsze pawda")

# liczba=int(input("Podaj liczbe:"))
# while liczba<=0:
#     liczba=int(input("Podaj liczbe jeszcze raz:"))

def powitanie():
    print("Czesc")

powitanie()

def powitanie_imienne(imie):
    print("Czesc,", imie)


def dzielenie(dzielna,dzielnik):
    if dzielnik==0:
        return 'BLAD'
    else:
        return dzielna/dzielnik
    
print(dzielenie(4,2))
x=dzielenie(4,2)
print(x)

lista=[1,2,3,4,4]
print(lista)
#print(*lista)
#print(*lista, sep=';')
print(type(lista))
lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.append(123)
print(lista)

print(lista[4])

lista[3]=32
print(lista)

lista.sort()
print(lista)

lista.count((4))
print(len(lista))

lista.remove(123)
print(lista)

tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)

print(len(tupla))
print(tupla.count(1))

print(tupla[0])
print(tupla[-2])

i=3
print(tupla[i:7])
print(tupla[3:])
print(tupla[:4])

#del tupla
#del lista
#print(lista)
krotka=(1,2,3)
a,b,c=krotka
print(a)
print(b)
print(c)

kontakty={
    "Jan":123456789,
    "Bogdan":213456789,
    "Borys":213456789
}

print(kontakty["Jan"])

for imie, numer in kontakty.items():
    print("%s ma numer telefonu: %d" %(imie, numer))

print(kontakty.keys())
print(kontakty.values())

zbior={1,2,3,4}

"""
f=open("text.txt", "r")
print(f.read())
f.close()

f=open("text.txt", "a")
f.write("ggg")
f.close()

f=open("text.txt", "a")
f.write("ggg")
f.close()

f=open("text.txt", "a")
print(f.read())

"""
