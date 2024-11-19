def get_multiplied_digits(number = input('Введите число: ')):
   number=int(number)
   str_number = str(number)
   if str_number.endswith('0'):
       str_number = str_number[:len(str_number) - 1]
   first = int(str_number[0])
   if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
   else:
        return first

result = get_multiplied_digits()
print('Результат: ', result)

#Павел Ившин
