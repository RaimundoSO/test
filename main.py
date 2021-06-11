#Un comentario solo para decir lo mal que está escrito esto
def abrirarchivo():
	archivo=input('Archivo: ')
	while True:
		try:
			arch=open(archivo)
			break
		except:
			print('El archivo no existe')
			archivo=input('Archivo: ')
	return arch
	
def probararchivo(arch):
	a=1
	cuenta=0
	for linea in arch:
		if a%7==1 and linea != '\n':
			a=a+1
		elif a%7==2 and linea.startswith('A. '):
			a=a+1
		elif a%7==3 and linea.startswith('B. '):
			a=a+1
		elif a%7==4 and linea.startswith('C. '):
			a=a+1
		elif a%7==5 and linea.startswith('D. '):
			a=a+1
		elif a%7==6 and linea.startswith('ANSWER:'):
			a=a+1
		elif a%7==0 and linea.startswith('\n'):
			a=a+1
		else:
			print('Hay un error en el archivo. Comprueba la línea', a)
			return False
	return True

def listacontenido(arch):
	import re
	preguntas=list()
	respuestaA=list()
	respuestaB=list()
	respuestaC=list()
	respuestaD=list()
	solucion=list()
	bloque=list()
	i=0
	for linea in arch:
		if re.findall('^A\.\s\S+',linea):
			respuestaA=respuestaA+re.findall('^A\.\s(.+$)',linea)
		elif re.findall('^B\.\s\S+',linea):
			respuestaB=respuestaB+re.findall('^B\.\s(.+$)',linea)
		elif re.findall('^C\.\s\S+',linea):
			respuestaC=respuestaC+re.findall('^C\.\s(.+$)',linea)
		elif re.findall('^D\.\s\S+',linea):
			respuestaD=respuestaD+re.findall('^D\.\s(.+$)',linea)
		elif re.findall('^ANSWER:\S',linea):
			solucion=solucion+re.findall('^ANSWER:(\S)',linea)
		elif linea != '\n':
			preguntas.append(linea.strip())
	for i in range(0,len(preguntas)):
		if solucion[i]=='A':
			respuestaA[i]=(respuestaA[i], 1)
			respuestaB[i]=(respuestaB[i], 0)
			respuestaC[i]=(respuestaC[i], 0)
			respuestaD[i]=(respuestaD[i], 0)
		elif solucion[i]=='B':
			respuestaA[i]=(respuestaA[i], 0)
			respuestaB[i]=(respuestaB[i], 1)
			respuestaC[i]=(respuestaC[i], 0)
			respuestaD[i]=(respuestaD[i], 0)
		elif solucion[i]=='C':
			respuestaA[i]=(respuestaA[i], 0)
			respuestaB[i]=(respuestaB[i], 0)
			respuestaC[i]=(respuestaC[i], 1)
			respuestaD[i]=(respuestaD[i], 0)
		elif solucion[i]=='D':
			respuestaA[i]=(respuestaA[i], 0)
			respuestaB[i]=(respuestaB[i], 0)
			respuestaC[i]=(respuestaC[i], 0)
			respuestaD[i]=(respuestaD[i], 1)
		bloque.append((preguntas[i], respuestaA[i], respuestaB[i], respuestaC[i], respuestaD[i]))	
	return bloque

def numpreguntas(bloque):
	print('Hay %d preguntas en el archivo' % len(bloque))
	num=input('Cantidad de preguntas deseadas: ')
	while True:
		try:
			num=int(num)
			if num>0 and num<=len(bloque):
				print('\n')
				return num
			else:
				print('Entrada no válida')
				num=input('Cantidad de preguntas deseadas: ')
				continue
		except:
			print('Entrada no válida')
			num=input('Cantidad de preguntas deseadas: ')
	
def cuestionario(bloque, num):
	import random
	cuenta=num
	aciertos=0
	while cuenta>0:
		aleat=random.randint(0, len(bloque)-1)
		lista=list(bloque[aleat])
		print(lista.pop(0))
		aleat2=random.randint(0,3)
		if lista[aleat2][1]==1:
			solucion='A'
		print('A.',lista[aleat2][0])
		del(lista[aleat2])
		aleat3=random.randint(0,2)
		if lista[aleat3][1]==1:
			solucion='B'
		print('B.',lista[aleat3][0])
		del(lista[aleat3])
		aleat4=random.randint(0,1)
		if lista[aleat4][1]==1:
			solucion='C'
		print('C.',lista[aleat4][0])
		del(lista[aleat4])
		if lista[0][1]==1:
			solucion='D'
		print('D.',lista[0][0])
		del(lista[0])
		resp=input('Tu respuesta: ')
		resp=resp.upper()
		if resp == solucion:
			print('Bien!\n')
			aciertos=aciertos+1
		else:
			print('Mal\n')
		cuenta=cuenta-1
		del bloque[aleat]
	return aciertos

archivo=abrirarchivo()
cosa=listacontenido(archivo)
numero=numpreguntas(cosa)
aciertos=cuestionario(cosa,numero)
print('Has acertado', aciertos, 'de',numero,'preguntas.')
