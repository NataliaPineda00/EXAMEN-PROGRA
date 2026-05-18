Algoritmo Tablas_de_multiplicar
	Definir limite_tablas, limite_numeros, resultado Como Entero
	
	Escribir "Ingrese un numero limite de tablas: "
	Leer limite_tablas
	Escribir "Ingrese un numero limite de casillas: "
	Leer limite_numeros
	
	Si limite_tablas <= 0 Entonces
		Escribir "El numero limite de tablas debe ser positivo, por favor vuelva a ingresar sus datos."
	FinSi
	
	Si limite_numeros <= 0 Entonces
		Escribir "El numero limite de casillas debe ser positivo, por favor vuelva a ingresar sus datos."
	FinSi
	
	Para limite_tablas  
		Escribir "Su resultado es: ", resultado 
	FinPara
		

	
	
	
FinAlgoritmo
