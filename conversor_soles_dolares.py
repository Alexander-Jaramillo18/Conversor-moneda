valordecambio = input("Que cantidad de dinero quieres cambiar \n ")
Tipodecambio = input("Quieres cambiar\n 1 De soles a dolares\n 2 de dolares a soles \n ")
valordecambio = int(valordecambio)
cambio=3.55
if Tipodecambio == "1":
    dolares=valordecambio/cambio
    dolares=round(dolares,2)
    print("Tienes "+ str(dolares) + " dolares")
else: 
    soles=valordecambio*cambio
    soles=round(soles,2)
    print("Tienes "+ str(soles)+ " soles")
