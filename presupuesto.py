'''
Pido los presupuestos de los cuatro primeros meses 
y los guardo en una variable con su nombre de mes, respectivamente.
'''

Enero = input("¿Cuál es tu presupuesto de Enero?: ")
Febrero  = input("¿Cuál es tu presupuesto de Febrero?: ")
Marzo = input("¿Cuál es tu presupuesto de Marzo?: ")
Abril = input("¿Cuál es tu presupuesto de Abril?: ")

#Convierto cada mes en un número flotante, pueden ser miles.
intEnero = float(Enero)
intFebrero = float(Febrero)
intMarzo = float(Marzo)
intAbril = float(Abril)

promedio = (intEnero+intFebrero+intMarzo+intAbril)/4
print(f"\n El presupuesto que puedes gastar en promedio es de ${promedio}, ¡Cuida tus finanzas!")
