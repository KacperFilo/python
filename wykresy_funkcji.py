import matplotlib.pyplot as p
import numpy as np

funkcja=["prosta","kwadratowa","homograficzna","logarytmiczna","sin","cos","tg","ctg","wykladnicza","wieloman trzeciego stopnia"]
while True:
    q=input("Podaj rodzaj funkcji:")
    if(q in funkcja): break

if q=="prosta":
   #a=(input("Podaj punkty osi x"))
   #b=(input("Podaj punkty osi y"))
   #p.plot([input("Podaj punkty osi x")], [input("Podaj punkty osi y")], 'ro-')
   p.plot([1,2,17,13], [10,5,6,19], 'ro-')
   p.axis([0, 20, 0, 20])
   p.grid()
   p.show()
   





