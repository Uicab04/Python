

# prediccion del tiempo:
import time
A = time.ctime()
A = A.split()
print(A)


hora=str(A[3])
grados="%garadodado"
prediccion_en10hras="tiempodado"
prediccion_mañana="DDDD"


def tiempo(nota):
    valoracion="Buen dia"
    if nota>12 and nota<20:
        valoracion="Buenas tardes"
    elif nota>19:
        valoracion="Buenas noches"
    return valoracion
print(tiempo(22))

mitupla="son las", "estamos a", "arrato estara", "y mañana sera"

# haciendo la frace
UI=(tiempo(22) + " " + str(mitupla[0]) + " " + str(hora) + ", " + str(mitupla[1]) + " " + str(grados) + ", " + 
      str(mitupla[2]) + " " + str(prediccion_en10hras) + ", " + str(mitupla[3]) + " " + str(prediccion_mañana) + ", ")

print(UI)