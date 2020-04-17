import random

r = random.randint(1,100)

while True:
	user_input = input('Please enter number: ')
	user_input = int(user_input)
	if user_input == r:
		print('Correct!')
		break
	elif user_input < r:
		print('Higher!')
	elif user_input > r:
		print('Lower!')
