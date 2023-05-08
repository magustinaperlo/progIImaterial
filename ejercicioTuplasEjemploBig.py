
# Supongamos que queremos almacenar información sobre varios empleados en una lista. 
# Cada empleado tiene un número de identificación, un nombre, un salario y una fecha de contratación.
#  Podríamos representar esta información utilizando tuplas, y luego almacenar las tuplas en una lista. 
#  Por ejemplo: 

empleado1 = (1, "Juan Perez", 3500, "01/01/2022")
empleado2 = (2, "Ana Rodriguez", 4500, "15/02/2022")
empleado3 = (3, "Pedro Gomez", 3000, "30/03/2022")

empleados = [empleado1, empleado2, empleado3]

""" En este ejemplo, cada tupla representa la información de un empleado, 
y las tres tuplas se almacenan en la lista "empleados".
Supongamos ahora que queremos acceder al salario del segundo empleado.
 Para hacer esto, podemos utilizar la sintaxis de indexación para acceder al segundo elemento de la lista 
 (que es la tupla que representa al segundo empleado), 
y luego acceder al tercer elemento de la tupla (que es el salario del empleado). Por ejemplo: """

salario_segundo_empleado = empleados[1][2]
print("El salario del segundo empleado es:", salario_segundo_empleado)

""" En este ejemplo, el código accede al segundo elemento de la lista "empleados" utilizando la sintaxis de indexación [1],
 lo que devuelve la tupla que representa al segundo empleado. Luego, el código accede al tercer elemento de la tupla 
 utilizando la sintaxis de indexación [2],
 que es el salario del empleado. Finalmente, se imprime el salario del segundo empleado por pantalla. """