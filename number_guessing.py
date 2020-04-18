import random
#let user set random number range
range_begin = input('Please enter number range from: ')
range_end = input('to: ')

r = random.randint(int(range_begin),int(range_end))
count = 0

while True:
	user_input = input('Please enter number: ')
	count += 1
	user_input = int(user_input) #casting
	if user_input == r:
		if count == 1:
			print('Correct!', count, 'guess')
		else: 
			print('Correct!', count, 'guesses')
		break
	elif user_input < r:
		print('Higher!')
	elif user_input > r:
		print('Lower!')
	print('Guess count: ', count)
