# Dia 8

print("Grades")

nota_alumno=int(input("Introduce tu nota: "))

if nota_alumno < 3:
    print("Insuficiente")
elif nota_alumno < 4:
    print("Aceptable")
elif nota_alumno < 5:
    print("Sobresaliente")
else:
    print("Excelente")