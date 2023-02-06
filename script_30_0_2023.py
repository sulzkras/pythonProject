# print('Hi Python!')
# userName = input('Enter your name:\t')
# print('Hi,', userName, '!', end = '\n', sep = '###')
# print(f'Hi, {userName}!')
# print(type(userName))

# print('Anyone who \n\tstops learning\n\t\t is old,\n\t\t\t whether at twenty or eighty.')
#
# numberOne = int(input('Enter number one: '))
# numberTwo = int(input('Enter number two: '))
# print('Сумма: ', numberOne + numberTwo)
# print('Разница: ', numberOne - numberTwo)
# print('Произведение: ', numberOne * numberTwo)
# print('**************************************')
# print(numberOne, '+', numberTwo, '=', numberOne + numberTwo)
# print(numberOne, '-', numberTwo, '=', numberOne - numberTwo)
# print(numberOne, '*', numberTwo, '=', numberOne * numberTwo)
#
# print('Результаты\n'
#       f'\t {numberOne} + {numberTwo} = {numberOne + numberTwo}')

#

# a = float(input('Введите катет А '))
# b = float(input('Введите катет В '))
# hypotenusa = (a ** 2 + b ** 2) ** 0.5
# print(hypotenusa)

# numberOne = int(input('Enter number one: '))
# numberTwo = int(input('Enter number two: '))
# print(numberOne/100*numberTwo)

# str1 = "Hello"
# str2 = "World"
# str3 = "!"
# print(str1 str2 + str3)

# x = int(input('Enter X '))
# y= int(input('Enter Y '))
# choc = int(input('Введите 1 для сложения\n'
#                  'Введите 2 для вычитания\n'
# 				'Введите 3 для умножения\n'
# 				'Введите 4 для деления\n'))
# if choc == 1:
# 	print(f" {x} + {y} = {x + y}")
# elif choc == 2:
# 	print(f" {x} - {y} = {x - y}")
# elif choc == 3:
# 	print(f" {x} * {y} = {x * y}")
# elif choc == 4:
# 	if y == 0:
# 		y = input('Y не может быть равен нулю')
# 	print(f" {x} / {y} = {x / y}")
# else:
# 	choc = int(input('Нужно ввести числа от 1 до 4'))
	
# if x > y:
# 	print(f'Число {x} больше числа {y}')
# elif y > x:
# 	print(f'Число {y} больше числа {x}')
# else:
# 	print('Числа равны')

# x = int(input('Enter any number: '))
# if x % 2 == 0:
# 	print(f'number {x} is event')
# else:
# 	print(f'number {x} is odd')
	
	
# D = int(input('Enter Diametr: '))
# choc = int(input('Введите 1 для площади\n'
#                  'Введите 2 для длины окружности\n'))
# if choc == 1:
# 	print(f" { 3.14 * (D / 2) ** 2}")
# elif choc == 2:
# 	print(f" {3.14 * D}")


# a = int(input())
# if a < -5:
#     print('Low')
# elif -5 <= a <= 5:
#     print('Mid')
# else:
#     print('High')


# number = 1
# while number <= 5:
# 	print(f'Iteration № {number}')
# 	number += 1


# x = int(input('Enter first number '))
# y = int(input('Enter second number '))
# firstNumber = x
# sum = 0
# while x <= y:
# 	print(x)
# 	sum += x
# 	x += 1
# print(f'Sum of all numbers betwent {firstNumber} and {y} is {sum}')


# for i in range(2, 15, 3):
# 	print(i)

# str = 'Какой-то текст'
# for i in str:
# 	print(i)

# for i in range(1, 10):
# 	for j in range(1, 10):
# 		if j == 9:
# 			print(i * j, end = '\n')
# 		else:
# 			print(i * j, end = '\t')


# import random
# finish = int(input('Введите номер этажа '))
# # lift = int(input('Введите номер этажа, где будет лифт '))
# floor = 1
# stamina = 70
# print(f'Я на {floor} этаже')
# lift = random.randint(2, finish -1)
# while floor != finish:
# 	step = 0
# 	while step != 20:
# 		step += 1
# 		stamina -= 1
# 		if stamina == 0:
# 			print(f'Я отдыхаю после {floor} этажа')
# 			stamina += 70
# 	floor += 1
# 	print(f'Я на {floor} этаже')
# 	if floor == lift:
# 		print(f'Я нашел лифт на {floor} этаже!')
# 		break
# 	# print(f'Я на {floor} этаже')
# print(f'Я достиг цели, я дошел до {floor} этажа')

# import turtle

# import random
# # Игра угадай число
#
# user_number = int(input('Угадайте число компьютера от 0 до 100: '))
# comp_number = random.randint(1, 100)
# print(f'computer number {comp_number}')
# while user_number != comp_number:
# 	# if user_number > comp_number:
# 	# 	print(f'Ваше число больше!')
# 	# 	user_number = int(input('от 0 до 100: '))
# 	if (comp_number - 4) < user_number < (comp_number + 4):
# 		print('Горячо!')
# 		user_number = int(input('от 0 до 100: '))
# 	elif (comp_number - 8) <= user_number <= (comp_number - 4) or (comp_number + 4) <= user_number <= (comp_number + 8):
# 		print('Тепло!')
# 		user_number = int(input('от 0 до 100: '))
# 	elif user_number < (comp_number - 8) or user_number > (comp_number + 8):
# 		print('Холодно!')
# 		user_number = int(input('от 0 до 100: '))
# 	# elif user_number < comp_number:
# 	# 	print(f'Ваше число меньше!')
# 	# 	user_number = int(input('от 0 до 100: '))
# print(f'Поздравляю, Вы угадали число {comp_number}!')

# try:
#   chisl = int(input('Enter any number: '))
# except ValueError:
#   print("You must enter number!")
#   chisl = int(input('Enter any number: '))

# while True:
#   try:
#     chisl1 = int(input('Enter any number 1: '))
#     chisl2 = int(input('Enter any number 2: '))
#     result = chisl1 / chisl2
#     print(result)
#     break
#   except ValueError:
#     print("You must enter number!")
#     chisl = int(input('Enter any number: '))
#   except ZeroDivisionError:
#     print('The number 2 can not be zero')
#
# print('')
  


# while True:
#   try:
#     apple = int(input('Enter number of apples: '))
#     if apple < 0:
#       raise Exception
#     print("It is OK")
#     break
#   except Exception:
#     print('You can not have minus of apples!')
# print("Exit")


str = 'Hello World!'
str2 = '123456789'
for i in str:
  print(i, end = '')
print(len(str))
print(str[2:5])
print(str[::-1])
print(str2[::2])
