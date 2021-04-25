import os

os.system("clear")
print("""__Bienvenido a este programa para cifrar-descifrar mensajes__

	""")
print("""Opciones:


1-Cifrar
2-Descifrar
3-Ayuda
4-Salir

""")

var=input("Elije una opcion: ")
while True:
	if var=="1":
		os.system("clear")
		#Funcion de cifrar donde necesita dos valores
		def cifrar(texto,clave):
		  longitud=len(texto); #Calculamos la longitud del texto para recorrerlo
		  for i in range (0,longitud): #Bucle para recorrer el texto
		    for pos in range (0,26): #Bucle para recorrer el Abecedario
		      if texto[i]==abc[pos]: #comparo las letras una por una
		        pos_abc=pos+int(clave) #Me desplazo en el abecedario en función a la clave
		        if pos_abc <26:
		           print(abc[pos_abc],end="")
		        if pos_abc >25 : #En el caso de que me pase del abecedario, calculo el modulo
		           print(abc[pos_abc%26],end="")
		    else:
		      print(end="")
		  return
		print("La utilidad de este programa consiste en cifrar el texto que introduzca mediante el método César.\n—————————————————–")
		texto=input("Dime el texto: ")
		clave=input("Dime la clave: ")
		abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]
		opcion=input("¿Quiere cifrar esto? [si/no] ")
		if opcion =="si" or opcion=="s":
		  cifrar(texto,clave) #llamo a la función pasándole el texto y la clave de cifrado
		  break
		else:
			os.system("clear")
			False
		

	elif var=="2":
		os.system("clear")
		#Funcion de descifrar donde necesita dos valores
		def descifrar(texto,clave):
		  longitud=len(texto);
		  for i in range (0,longitud):
		    for pos in range (0,26):
		      if texto[i]==abc[pos]:
		        pos_abc=pos-(int(clave))
		        if pos_abc >-1:
		           print(abc[pos_abc],end="")
		        if pos_abc <0 :
		           print(abc[pos_abc%26],end="")
		    else:
		      print(end="")
		  return
		print("La utilidad de este programa consiste en descifrar el texto que introduzca mediante el método César.\n—————————————————–")
		texto=input("Dime el texto: ")
		clave=input("Dime la clave: ")
		abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]
		opcion=input("¿Quiere descifrar esto? [si/no] ")
		if opcion =="si" or opcion=="s":
		  descifrar(texto,clave) #llamo a la función pasándole el texto y la clave de cifrado
		  break
		else:
			print("ERROR")
			os.system("clear")
			False
	elif var=="3":
		os.system("clear")
		print("""__Cifrador/Descifrador__ Version: 2.0

Programa que cifra o decifra mensajes usando el metodo Cesar, para mas informacion https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

""")
		break
	elif var=="4":
		os.system("clear")
		print("Hasta luego ")
		break
	else:
		break
