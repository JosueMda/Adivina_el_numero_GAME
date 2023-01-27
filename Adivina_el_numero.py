""" ADIVINA EL NUMERO: UN JUEGO DESARROLLADO PARA PRACTICAR EL USO DE FUNCIONES. ESTE CONSISTE EN ACERTAR 
EN MENOS DE CINCO INTENTOS EL NUMERO QUE HA GENERADO PYTHON ALEATORIAMENTE POR MEDIO DEL MODULO RANDOM"""


from random import randint

def var1():
  secreto = randint(1, 20)
  #print(secreto)
  nombre = input(
    '\n***BIENVENIDO***\nIngresa tu nombre para comenzar a jugar aca -> ')
  print(
    f'\nHola {nombre}, estoy pensando un numero del 1 al 20\nTe dare 5 intentos para que lo adivines\n\n*****   EMPECEMOS!!  *****\n'
  )
  num = int(input("Arriesgue un numero: "))
  lista = [num]

  for n in range(4):
    if num < secreto:
      print(
        "\nMmmm te falta para llegar al numero que pense, ingresa un numero mas alto: "
      )
      num = int(input("Arriesgue un numero: "))
      lista.append(num)
    elif num > secreto:
      print("\nAh! Te has pasado, intenta con un numero mas bajo: ")
      num = int(input("Arriesgue un numero: "))
      lista.append(num)
  if secreto in lista:
    print(
      f"\n*****HAS GANADO*****\n\nLOGRASTE VENCERME EN {len(lista)} INTENTOS\n\nFELICITACIONES\n"
    )
  else:
    print("\nHAS PERDIDO\nNO HAS PODIDO SUPERARME, HUMANO\n")


var1()
desafio = int(
  input(
    "Deseas volver a desafiarme?\nSI --> INGRESA 1\nNO --> INGRESA 2\nRESPUESTA: "
  ))
while desafio == 1:
  var1()
  desafio = int(
    input("Deseas volver a desafiarme?\nSI --> INGRESA 1\nNO --> INGRESA 2\n"))
else:
  print("HASTA LUEGO, COBARDE")
