materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
#recorrer materias como materia
for matteria in materias:
    calificaion = input("¿Que nota has sacado en " + materia + "?")
    notas.append(calificacion)
for i in range(len(materias)):
    print("En " +materias[i] + "has sacado" + notas[i])
    