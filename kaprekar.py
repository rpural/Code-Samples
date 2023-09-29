''' Kaprekar's Constant (6174)

Choose any 4 digit random number, having
a minimum of two unique digits.

Arange the digits in decending order and
again in ascending order. Subtract the
second from the first. Do this repeatedly,
and you'll arrive at 6174. If you do this
with 6174, you'll get 6174 again.
'''

def kaprekar(value):
	svalue = [ch for ch in str(("000"+str(value))[-4:])]
	unique = set(svalue)
	if len(unique) == 1:
		return None
	svalue.sort()
	lowvalue = int(str("".join(svalue)))
	highvalue = int(str("".join(svalue[::-1])))
	return highvalue - lowvalue
	
if __name__ == "__main__":
	print(f"kaprekar(6174) == {kaprekar(6174)}")
	
	value = -1
	while value != 0:
		value = input("Enter a 4 digit number: ")
		if value == "0":
			break
		while value != 6174:
			value = kaprekar(value)
			print(f"--> {value}")

	
