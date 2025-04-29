# Se importa "re" para usar expresiones regulares
import re
# Se definen las variables y se le asigna el tipo
grade:float
grades:list[float]
strGrade:str
userGrade:str
average:float
value:float
i:int
higherGrades:list[float]
specificGrade:float
# Se valida que esté en un rango de 0 a 100
print('\nDETERMINAR EL ESTADO DE APROBACIÓN\n')
def alert():
        print('El numero ingresado es incorrecto, ingresalo nuevamente')
while True:
    try:
        grade = float(input('Ingresa una calificación: '))
        if 0 <= grade <= 100: break
        else: alert()
    except ValueError: alert()
# Se valida el estado de aprobación
if grade >= 70:
    print('\nAprobado\n')
elif grade >= 50 < 70:
    print('\nRegular\n')
else: print('\nReprobado\n')
# Se calcula el promedio de acuerdo a las calificaciones que se ingresen
print('CALCULAR EL PROMEDIO\n')
grades = []
strGrade = ''
userGrade = input(f'Ingrese las calificaciones separada por comas (Ej: "5,6,4.5,3"): ')
# Se recorren las calificaciones con un "for" para agregar cada una a la lista "grades"
for c in userGrade:
    if c == ',':
        grades.append(float(re.sub(r'\D','',strGrade)))
        strGrade = ''
    else:
        strGrade += c
grades.append(float(re.sub(r'\D','',strGrade)))
average = sum(grades) / len(grades)
print(f'Tus calificaciones son: {grades}')
print(f'\nEl promedio de las calificaciones es: {average}\n')
# Se ingresa el valor especificado
print('CONTAR CALIFICACIONES MAYORES\n')
while True:
    try:
        value = float(input('Ingresa un valor especifico para compararlo con tus calificaciones: '))
        break
    except ValueError: alert()
# Se recorre la lista "grades" con un "while" para contar cuántas calificaciones son mayores que el valor especificado
i = 0
higherGrades = []
while i < len(grades):
    if grades[i] > value:
        higherGrades.append(grades[i])
    i += 1
print(f'\nHay {len(higherGrades)} calificacion/es mayor/es al valor especificado: {higherGrades}\n')
# Se ingresa la calificación específica
print('VERIFICACIÓN Y CONTEO\n')
while True:
    try:
        specificGrade = float(input('Ingresa la calificación especifica que deseas encontrar: \n'))
        break
    except ValueError: alert()
# Se utiliza el "for" para recorrer la lista "grades" y poder encontrar las coincidencias de una calificación específica
i = 0
for c in grades:
    if c == specificGrade:
        i += 1
        continue
print(f'Se encontro/aron {i} coincidencia/s de tu calificación {specificGrade} en la lista {grades}')