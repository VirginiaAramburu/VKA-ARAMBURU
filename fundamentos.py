def nuevotema(tema:str):
   print("\n-----", tema, "-----\n") 


if __name__ =="__main__":


    #TAREA 1
    #EJERCICIO 1 OPERADORES ARITMETICOS 
    nuevotema("OPERADORES ARITMETICOS")
    print("OPERADOR SUMA ,5+6=", 5+6)
    print("OPERADOR RESTA ,56-6=" ,56-6)
    print("OPERADOR MULTIPLICACION ,15 * 15=",15*15)
    print("OPERRADOR DIVISION, 15/3= ",15/3)
    print("OPERADOR RESIDUO,16%3=", 16%3)
    print("OPERADOR POTENCIA, 2**3=",2**3)
    print("OPERADOR CAMBIO DE SIGNO, -45= ", -45)


    #EJERCICIO 2 HACER LAS TABLAS DE VERDAD
    nuevotema("OPERADORES LOGICOS")
    print("TABLA DE VERDAD AND")
    print("True and True =",True and True )
    print("True and False  =",True and False )
    print("False and True =",False and True )
    print("False and False =",False and False )

    print ("TABLA DE VERDAD NOT")
    print (" not False  =", not False )
    print (" not True =", not True )
    
    print("TABLA DE VERDAD OR")
    print("True or True =",True or True )
    print("True or False  =",True or False )
    print("False or True =",False or True )
    print("False or False =",False or False )

    # EJERCICIO 3 UN EJEMPLO POR CADA OPERADOR DE COMPARACION
    nuevotema("OPERADORES DE COMPARACION")
    print("10 == 7:", 10 == 7)  # Igualdad
    print("10 != 7:", 10 != 7)  # Desigualdad
    print("10 >  7:", 10 > 7)   # Mayor que
    print("10 <  7:", 10 < 7)   # Menor que
    print("10 >= 7:", 10 >= 7)  # Mayor o igual que
    print("10 <= 7:", 10 <= 7)  # Menor o igual que

    # EJERCICIO EN CLASE
    nuevotema("VARIABLES")
    variable=10
    _variable2=6.25
    Variable3= "pepe"
    variable
    nombreVariable =8
    nombre_variable= 34.2

    print(variable , _variable2,Variable3,nombreVariable,nombre_variable)

    a,b,c =5, 10.8 , "Vicka"

    print(a)
    print(b)
    print (c)
        
    print(nombre_variable)

    nuevotema("ENTEROS")
    w=105
    x= 12345678910111213
    y= -58
    z= 0b00110011
    h= 0xFF
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevotema("flotantes")
    x=1234.56
    print(x, type(x))
    y= -0.025
    print(y , type (y))

    nuevotema("numeros complejos")
    x= -46j
    y= 12+45j
    z= 2j
    c= y +z

    print(x, type(x))
    print(y , type(y))
    print(z, type(z))
    print(c, type(c))

    nuevotema("Booleanos")

    x = True
       
    print(x, type(x))
    
    nuevotema("listas")
    lista =[10 , 20.5, "lista de python"]
    print(lista)
    print(lista[1])
    #imprime la posicion 1
    lista[0] ="Vicka"
    #reemplaza la posicioncero por el texto
    print(lista)
    lista.append(34)
    # aumenta un ultimo valor a la lista
    print (lista)
    lista.insert(0, 1.1)
    print(lista)
    lista.append([3,4,5,6,7,9])
    #se agrega el elemento 5 (esta sublista)
    print(lista)
    print([5])
    #imprime la lista dentro de la lisa)
    print(lista [5] [4])
    #imprime  de la lisa dentro  de la lista la posicion 4
    print (lista [3] [2])
    #regresa del campo 3 que es el texto la posicion 2

    nuevotema("TUPLAS")
    tupla= (25,"Tupla", 5 + 10j)
    #una vez creada la tupla no le podemos cambiar el valor
    print(tupla)
    
    tupla= (25,"Tupla", 5 + 10j, "otro")
    #se agrego un nuevo elemento, pero se crea uno nuevo
    print(tupla)
    #tupla[0]= 0 no es valido porque ya estaba establecido

    nuevotema =("CONJUNTOS")
    conjunto=  {10,20,30,40,50}  
    print (conjunto)
    print(conjunto)
    conjunto.add(80)

    nuevotema = ("DICCIONARIOS")
    diccionario = {"nombre": "conrado",
                   "edad" :41,
                  "telefono": 123456789 }
    
    print (diccionario)
    print (diccionario ["nombre"])
    

    nuevotema=("CADENAS")
    cadena1= "esto es una cadena"
    cadena2= "esto es otra cadena"
    cadena_multilinea='''esto es una cadena con tabuladores         y saltos
    de 
    linea'''
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena_multilinea, type(cadena_multilinea))
    cadena3="hola"* 5
    print(cadena3)
    print(cadena1 [2])
    print(cadena1 [2:10])
    print(cadena1 [:5])
    #desde el principio a la posicion 5
    print(cadena1 [5:])
    #desde el 5 al final




