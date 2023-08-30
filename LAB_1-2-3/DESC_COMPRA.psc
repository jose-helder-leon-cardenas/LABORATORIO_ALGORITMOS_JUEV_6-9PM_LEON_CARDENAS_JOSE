Algoritmo DESC_COMPRA
	
	Escribir "INGRESE EL MONTO DE LA COMPRA TOTAL"
	LEER CompraTotal
	
	si CompraTotal >= 3000 Entonces
		desc = CompraTotal*(0.1)
		pagofinal =CompraTotal - desc
		Escribir "el pago final es de: " , pagofinal
	SiNo
		descuento = CompraTotal*(0.05)
		pagofinal = CompraTotal - descuento
		Escribir " el pado con descuento es de: ", pagofinal	
	FinSi
	
FinAlgoritmo
