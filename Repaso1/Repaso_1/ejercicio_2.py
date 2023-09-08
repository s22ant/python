persona = {}
continuar = True
while continuar:
    #puedes cargar cualquier dato sobre una persona en el formato calve:valor
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    peraona[clave] = valor
    print(persona)
    #Tienes que escribir si para coninuar, en cualquier otro caso es False
    coninuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
    