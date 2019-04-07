from stack import Stack

def is_match(val1, val2):
	if val1 == "{" and val2 == "}":
		return True
	elif val1 == "[" and val2 == "]":
		return True
	elif val1 == "(" and val2 == ")":
		return True
	else:
		return False


def balanced_paran(paran_string):
	s = Stack()
	is_balanced = True
	index = 0

	while index < len(paran_string) and is_balanced:
		paran = paran_string[index]

		if paran in "{[(":
			s.push(paran)
		else:
			if s.is_empty():
				is_balanced = False
			else:
				top = s.pop()
				if not is_match(top, paran):
					is_balanced = False

		index += 1

	if s.is_empty() and is_balanced:
		return True
	else:
		return False


print(balanced_paran("[[]]"))
print(balanced_paran("{{[()"))
