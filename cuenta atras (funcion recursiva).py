#Funciones RECURSIVAS
def cuenta_atras (n):
    if n < 0:
        print("Fin")
    else:
        print(n)
        n -= 1
        cuenta_atras(n)

cuenta_atras(10)