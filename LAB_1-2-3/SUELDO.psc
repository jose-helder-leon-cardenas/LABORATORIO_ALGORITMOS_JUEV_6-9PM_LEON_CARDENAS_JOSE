Algoritmo cal_sueldo_neto
	//sueldo total o sueldo basico en peru
	ST <- 1000
	
	//para calcular el descuento de IGV
	IGV = (ST-ST*0.11)
	Escribir "el igv(AFP) es de : ", ST*0.11
	Escribir "con el decuento de igv es de : ", IGV
	
	
	//Para calcular el adelanto en la quincena
	Q = ST/2
	Escribir  "Adelanto quincenal : ", Q	
	
	// Para calcular el 30% del Q 
	QT =Q*0.30  //quincena total
	Escribir "sueldo de adelanto quincenal total: ", QT
	
	//sueldo final obtenido
	SN = QT + IGV
	
	Escribir  "el sueldo neto es de : ", SN
	
	Escribir "//////////////////////////////"
	//LO CORRECTO SERIA :
	
	sueldo_basico <- 930
	descuento_afp = sueldo_basico*0.11
	descuento_quincenal = sueldo_basico*0.33
	
	sueldo_neto = sueldo_basico -descuento_afp-descuento_quincenal
	Escribir "AL FINAL DEL MES RECIBE :" , sueldo_neto
	
FinAlgoritmo
