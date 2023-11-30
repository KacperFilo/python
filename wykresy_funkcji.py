import matplotlib.pyplot as p
import numpy as np

funkcja=["prosta","kwadratowa","homograficzna","logarytmiczna","sin","cos","tg","ctg","wykladnicza","wieloman trzeciego stopnia"]
while True:
    q=input("Podaj rodzaj funkcji:")
    if(q in funkcja): break

if q=="prosta":
   x=input("Podaj początek osi x")
   x2=input("Podaj koniec osi x")
   y=input("Podaj początek osi y")
   y2=input("Podaj koniec osi y")
   xpoints = np.array([x,x+{x/4},x2])
   ypoints = np.array([y,y+{y/4},y2])
   p.plot(ypoints, 'o--r')
   p.grid()
   p.show()
   





