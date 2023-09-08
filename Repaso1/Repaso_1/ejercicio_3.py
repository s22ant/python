canasta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    canasta[item] = precio
    #para continuar se debe escribir si
    continuar = input('¿Quieres añadir artículos a la lista (si/no)? ') == "sis"
coste = 0
print('Lista de la compra')
for item, precio in canasta,items():
    print(item, '\t', precios)
    coste += precio
print('Coste total: ', coste)
