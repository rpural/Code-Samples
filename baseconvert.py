''' Convert a decimal number from or 
	to another base '''

_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

class BaseError (Exception):
	''' BaseError: in to or from_base(), the
	base must be between 2 and 60. '''
	pass
	
def to_base(value,newbase):	
	''' to_base(value, base)
		given a base between 2 and 60,
		convert a value from base 10 to
		the new base. '''
	if not 2 <= newbase <= 60:
		raise BaseError("Base out of range")
	stack = []
	while value > 0:
		digit = value % newbase
		stack.append(digit)
		value //= newbase
		
	result = ""
	while len(stack) > 0:
		digit = stack.pop()
		result += _digits[digit]
		
	return result
	
def from_base(value, oldbase):
	''' from_base(value, base)
		Given a string representing a 
		value in the given base, convert
		the value to base 10. '''
	if not 2 <= oldbase <= 60:
		raise BaseError("Base out of range")
	exponent = 1
	result = 0
	for digit in value[::-1]:
		digit_value = _digits.index(digit)
		if digit_value > oldbase:
			raise ValueError("Value out of range for base")
		result += (digit_value * exponent)
		exponent *= oldbase
	return result
	
	
def convert_base(value, from_, to):
	standard = from_base(value, from_)
	return to_base(standard, to)
	
	
if __name__ == "__main__":
	test_to_bases = (10, 8, 2, 16, 35, 50, 52)
	test_to_values = (5, 10, 50, 500, 5_000, 123_456)
	
	test_from = {10: ('5', '10', '50', '500', '5000', '123456'), 
			8: ('5', '10', '50', '500', '5000', '123456'),
			2: ('101', '1101', '111'),
			16: ('F', '10', '1D', '1000'), 
			35: ('5', '10', '50', '500', '5000', '123456'), 
			50: ('5', '10', '50', '500', '5000', '123456'), 
			52: ('5', '10', '50', '500', '5000', '123456', '12ABab')
		}
		
	test_convert = {'101': ((2,10), (2,8), (2,16)),
			'70': ((8,10), (8,2), (8,16)),
			'1F': ((16,10), (16,8), (16,2)),
			'1f': ((52,10), (52,30), (52,60))
			}
	
	for base in test_to_bases:
		print(f"\nconverting to base {base}:")
		for value in test_to_values:
			print(f"  {value} = {to_base(value, base)}")
			
	for base in test_from.keys():
		print(f"\nconverting from base {base}:")
		for value in test_from[base]:
			print(f"  {value} = {from_base(value, base)}")
			
	print()	
	for value in test_convert.keys():
		for from_, to in test_convert[value]:
			print(f"{value} from {from_} to {to} = {convert_base(value, from_, to)}")
	
	print()
	try:
		x = to_base(66, 66)	
	except BaseError as e:	
		print(f"error: {e}")
		
	try:
		x = from_base('66', 66)
	except BaseError as e:
		print(f"error: {e}")
		
	try:
		x = from_base('12fgABz', 40)
	except ValueError as e:
		print(f"error: {e}")
