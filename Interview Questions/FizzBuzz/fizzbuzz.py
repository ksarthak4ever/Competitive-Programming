for input in range(1,100): #in this case complexity would be 0(1)

	if input % 3 == 0 and input % 5 == 0:
		print('FizzBuzz')
	elif input % 3 == 0:
		print('Fizz')
	elif input % 5 == 0:
		print('Buzz')
	else:
		print(input)


'''
def fizzbuzz(input):

	if input % 3 == 0 and input % 5 == 0:
		return "FizzBuzz"

	if input % 3 == 0:
		return "Fizz"

	if input % 5 == 0:
		return "Buzz"


print(fizzbuzz(15))

#Complexity would be 0(1) for space and time
'''