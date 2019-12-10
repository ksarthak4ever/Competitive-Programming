for input in range(1,100): #in this case complexity would be 0(1)

        c1 = input % 3 == 0
        c2 = input % 5 == 0

        if c1 or c2: 
            print(c1*"Fizz"+c2*"Buzz")
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
