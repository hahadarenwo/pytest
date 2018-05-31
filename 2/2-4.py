age = int(input('age:'))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

height = 1.75
weight = 80.5
bmi = weight / height / height
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('normal')
elif 25 <= bmi < 28:
    print('fat')
elif 28 <= bmi < 32:
    print('obesity')
else:
    print('Severe obesity')
