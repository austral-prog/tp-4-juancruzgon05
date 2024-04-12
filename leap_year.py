def leap_year():
    num=int(input("Ingrese un año:"))
	if (num %4==0 and not num %100==0) or (num %100==0 and num%400==0): 
		print(f"El año {num} es bisiesto")
	else:
		print(f"El año {num} no es bisiesto")
