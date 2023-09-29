'''
For beginners. A little coding task to practice detecting different types of item in a list, and handling them appropriately. Given this list: [102, 6.6, '77', '564', 75, '3.92', 'E', 2.77, 7.66, 'C', '408',          605, '690', 'Z', '134', 'S', 'K', 148, '68', '654', 'U', '537',          0.64, 905, 5.75, 302, '7.57', '834', '0.64', '29', '709', '8.28',          'Y', 640, 'U', '0.92', 4.63, '259', '245', '5.1', 'Z', 'D',          '5.58', 1.26, 6.95, '2.87', '9.25', 'F', 273, '852'] write a script to add up all the integers into one total, and all the float values into a second total, but recognising that some integers and floats may be present in strings, (e.g. in the last line '5.58' and 1.26 are both to be handled as floats, and 273 and '852' both represent integer values). Any strings that do not contain integers or floats are to be concatinated into a single string. Print the total value of integers, the total value of floats, and the concatinated string.
'''

class ForceFloat(Exception):
	pass

sample = [102,6.6,'77','564',75,'3.92','E', 
			2.77,7.66,'C','408',605,'690','Z',
			605,'134','S','K',148,'68','654',
			'U','537',0.64,905,5.75,302,'7.57', 
			'834','0.64','29','709','8.28','Y',
			640,'U','0.92',4.63,'259','245', 
			'5.1','Z','D','5.58',1.26,6.95, 
			'2.87','9.25','F',273,'852']

totflt = (6.6+3.92+2.77+7.66+0.64+5.75+7.57+
		0.64+8.28+0.92+4.63+5.1+5.58+1.26+6.95+
		2.87+9.25)			
totint = (102+77+564+75+408+605+690+605+134+148+
		68+654+537+905+302+834+29+709+640+259+
		245+273+852)
print(f"actual int total: {totint}, float total: {totflt}")
			
def ints_and_floats_sum(sample):
	ints = 0
	floats = 0
	
	for value in sample:
		try:
			if "." in str(value):
				raise ForceFloat
			ints += int(value)
		except (ValueError, ForceFloat):
			try:
				floats += float(value)
			except ValueError:
				pass
	return (ints, floats)
	
sums = ints_and_floats_sum(sample)
print(f"int sum: {sums[0]}, float sum: {sums[1]}")
# output: int sum: 9061, float sum: 80.39
