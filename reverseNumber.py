"""
🐍 PYTHON CODING CHALLENGE - TWIST NUMBERS

# print out the reverse of the number with each digit doubled

# example 426 ->(reverse) 624 -> (double) 1248

numbers = [34, 243, 659, 517, 8, 47]

#output

'The twisted numbers are: 86, 684, 181012, 14210, 16, 148'

-----------------

PLEASE SHARE code in EDITABLE & ’Runnable’ format for others to play with. (e.g. carbon.now.sh/ pastebin.com ) or paste code in comment and include pic for indents

Discuss different solutions and help each other👍

Extra points for not using imports

Have fun!
"""

numbers = [34, 243, 659, 517, 8, 47]
solutions = [86, 684, 181012, 14210, 16, 148]


def reverseNumber(value):
	solution = 0
	while value > 0:
		digit = (value % 10) * 2
		solution *= 10
		if digit > 9:
			solution *= 10
		solution += digit
		value //= 10
	return solution
	
for i, correct in zip(numbers, solutions):
	result = reverseNumber(i)
	if result == correct:
		print(f"{i:4}: {result:6}")
	else:
		print(f"{i:4}: {result:6} - expected {correct:6}")
