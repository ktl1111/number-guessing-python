import random

r = random.randint(1,100)
count = 0

while True:
	user_input = input('Please enter number: ')
	count += 1
	user_input = int(user_input) #casting
	if user_input == r:
		print('Correct!', count, 'times guessing')
		break
	elif user_input < r:
		print('Higher!')
	elif user_input > r:
		print('Lower!')
	print('Guess count: ', count)
