def fizzbuzz(input):

	if input % 3 == 0 and input % 5 == 0:
		return "FizzBuzz"

	if input % 3 == 0:
		return "Fizz"

	if input % 5 == 0:
		return "Buzz"


print(fizzbuzz(15))



#Complexity would be 0(1) for space and time
