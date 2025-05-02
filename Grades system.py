# Se importa "re" para usar expresiones regulares
import re
# Se definen las variables y se le asigna el tipo
grade: float
grades: list[float]
str_grade: str
user_grade: str
average: float
value: float
i: int
higher_grades: list[float]
specific_grade: float
# Se valida que esté en un rango de 0 a 100
print('\nDETERMINAR EL ESTADO DE APROBACIÓN\n')
# Solo se crea una función únicamente para mostrar un mensaje de alerta
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
str_grade = ''
user_grade = input(f'Ingrese las calificaciones separada por comas (Ej: "5,6,4.5,3"): ')
# Se recorren las calificaciones con un "for" para agregar cada una a la lista "grades"
for c in user_grade:
    if c == ',':
        grades.append(float(re.sub(r'[^\d.]','',str_grade)))
        str_grade = ''
    else:
        str_grade += c
grades.append(float(re.sub(r'[^\d.]','',str_grade)))
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
higher_grades = []
while i < len(grades):
    if grades[i] > value:
        higher_grades.append(grades[i])
    i += 1
print(f'\nHay {len(higher_grades)} calificación/es mayor/es al valor especificado: {higher_grades}\n')
# Se ingresa la calificación específica
print('VERIFICACIÓN Y CONTEO\n')
while True:
    try:
        specific_grade = float(input('Ingresa la calificación especifica que deseas encontrar: \n'))
        break
    except ValueError: alert()
# Se utiliza el "for" para recorrer la lista "grades" y poder encontrar las coincidencias de una calificación específica
i = 0
for c in grades:
    if c == specific_grade:
        i += 1
        continue
print(f'Se encontró/aron {i} coincidencia/s de tu calificación {specific_grade} en la lista {grades}')