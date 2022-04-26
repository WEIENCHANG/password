password = 'a123456'
x = 3
while x > 0:
	mode = input('please enter your password: ')
	if mode == 'a123456':
		print('PASS')
		break
	else:
		print('WRONG')
		x = x - 1
		y = str(x)
		print('you stil have', y, 'chance')
print('bye')
