def insertion_sort(collection):
	length = len(collection)
	for index in range(1,length):
		while 0 < index and collection[index] < collection[index - 1]:
			collection[index],collection[index-1] = collection[index-1],collection[index]
			index = index-1
	return collection

if __name__ == '__main__':
	user_input = input('Enter numbers separated by a comma:\n').strip()
	unsorted = [int(item) for item in user_input.split(',')]
	print(insertion_sort(unsorted))