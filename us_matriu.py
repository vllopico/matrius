from matriu import matriu

l_a = [[2,0,1],[3,0,0],[5,1,1]]
l_b = [[2,0,1],[3,0,0]]

#Objectes
a = matriu(l_a)
b = matriu(l_b)

#Imprimir
print("Imprimir a i b")
a.imprimir_matriu()
b.imprimir_matriu()

#Sumar
print("Imprimint la suma de a i b")
a.suma_matriu(b)
a.imprimir_matriu()

#Resta
print("Imprimint la resta de a i b")
a.suma_matriu(b)
a.imprimir_matriu()

#Escalar
print("Imprimint l'escalar de a i 2")
a.escalar(2)
a.imprimir_matriu()


#Multiplicacio
a.multiplica_matriu(b)
a.imprimir_matriu()


#Divisio
print("Divisió entre a i b")
a.divisio_matriu(b)
a.imprimir_matriu()

#Error_1
l_e1 = [1,2,3]
e1 = matriu(l_e1)

#Error_2
l_e2 = [["a", "n"], [1,2]]
e2 = matriu(l_e2)



