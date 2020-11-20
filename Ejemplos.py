#Ejercicio 1
cap=float(input("Ingrese la capital invertida: "))
gan=(cap*0.02)
print(f"El total de la ganancia es de: {gan}")
#Ejercicio 2
sb=float(input("Ingrese su salario base: "))
v1=float(input("Ingrese la venta 1: "))
v2=float(input("Ingrese la venta 2: "))
v3=float(input("Ingrese la venta 3: "))
tventas=(v1+v2+v3)
com=tventas*0.10
sbtot=com+sb
print(f"El total ganado por comisión es: {com}")
print(f"El total del sueldo es de: {sbtot}")
#Ejercicio 3
precio=float(input("Digite el precio: "))
descuento= precio*0.15
precio_final= precio-descuento
print(f"El precio final a pagar es de ${precio_final:.2f}")
#Ejercicio 4
cal1=float(input("Ingrese la calificación del primer parcial: "))
cal2=float(input("Ingrese la calificación del segundo parcial: "))
cal3=float(input("Ingrese la calificación del tercer parcial: "))
ef=float(input("Ingrese la calificación del exámen final: "))
tf=float(input("Ingrese la calificación del trabajo final: "))
prom=(cal1+cal2+cal3)/3
p_par=prom*0.55
p_ef=ef*0.30
p_tf=tf*0.15
calf=p_par+p_ef+p_tf
print(f"La calificación final es: {calf:.2f}")
#Ejercicio 5
num_h=float(input("Ingrese el número de hombres: "))
num_m=float(input("Ingrese el número de mujeres: "))
tot_est=num_h+num_m
por_h=((num_h*100)/tot_est)
por_m=((num_m*100)/tot_est)
print("El total de estudiantes es de",tot_est)
print(f"El porcentaje de hombres que hay en el grupo es del {por_h:.2f}%")
print(f"El porcentaje de mujeres que hay en el grupo es del {por_m:.2f}%")
#Ejercicio 6
año_nac=int(input("Digite su año de nacimiento: "))
año_act=int(input("Digite el año actual: "))
edad=año_act-año_nac
print(f"Usted tiene {edad} años")