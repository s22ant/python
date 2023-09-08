#esto es una lista
dia_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado'; 'Domingo']

#imprimir los datos de una lista con un for
print("Dias de la semana")
for dia in dias_semana:
    print(dia)

#esto es un diccionario de alumnos con sus calificaciones
calificaciones = {"Pepe":[2,4,5],"juan":[3,4,4],"Moises":[4,3,5]}
print("Lista de alumnos")
for c in calificaciones:
    print(c)

print("Lista de alumnos y promedio de calificaciones")
for i in calificaciones[c]:
    suma +=1
print('prom: {0}'.format((suma/len(calificaciones[c]))))

#tuplas, semejante a las listas pero inmutables
print('Mese del año')
meses = ('enero','febrero','marzo','abril','mayo')
for mes in meses:
    print(mes)

#otra lista, y los métodos de las lista
precios = [4500,1200,3600,8000]
print(precios)
#agregar elementos a la lista
precios.append(900)
print(precios)
#quitar el último elemento
print(precios.pop())
print(precios)
