# Se definen las variables y se le asigna el tipo
grade:float
grades:list[float]
gradeStr:str
average:float
buffer:str
# Se valida que este en un rango de 0 a 100
print('Determinar el estado de aprobacion:\n')
def alert():
        print('El numero ingresado es incorrecto, ingresalo nuevamente')
while True:
    try:
        grade = float(input('Ingresa una calificacion: '))
        if 0 <= grade <= 100: break
        else: alert()
    except ValueError: alert()
# Se valida el estado de aprobacion
if grade >= 70:
    print('Aprobado\n')
elif grade >= 50 < 70:
    print('Regular\n')
else: print('Reprobado\n')
# Se calcula el promedio de acuerdo a las calificaciones que se ingresen, tiene un limite de 4 calificaciones
print('Calcular el promedio:\n')
grades = []
buffer = ''
gradeStr = input(f'Ingrese la calificacion separada por comas (Ex: "5,6,4.5,3"): ')
for c in gradeStr:
    if c == ',':
        grades.append(float(buffer.replace('\D','')))
        buffer = ''
    else:
        buffer += c
grades.append(float(buffer))
average = sum(grades) / 4
print(f'El promedio de las calificaciones es: {average}\n')
print(grades)
# Se ingresa el valor especificado
print('Contar calificaciones mayores:\n')
value:float = float(input('Ingresa un valor especifico para compararlo con tus calificaiones: '))