'''
Re-visiting an old but fun challenge. Write a script to express any positive number in the range 0 to 9999 inclusive, in English words.

Examples:
0 : zero
1000 : one thousand
3019 : three thousand and nineteen
234 : two hundred and thirty four
'''

def toText(value : int) -> str:
	try:
		x = toText.texts[1]
	except AttributeError:
		# define texts for use in the output one time
		toText.texts = { 1: "one",
			2: "two",
			3: "three",
			4: "four",
			5: "five",
			6: "six",
			7: "seven",
			8: "eight",
			9: "nine",
			10: "ten",
			11: "eleven",
			12: "twelve",
			13: "thirteen",
			14: "fourteen",
			15: "fifteen",
			16: "sixteen",
			17: "seventeen",
			18: "eighteen",
			19: "ninteen",
			20: "twenty",
			30: "thirty",
			40: "forty",
			50: "fifty",
			60: "sixty",
			70: "seventy",
			80: "eighty",
			90: "ninty", }
		toText.positions = {1: "",
			2: "thousand",
			3: "million",
			4: "billion",
			5: "trilion",
			}
	breaks = []
	while value > 0:
		breaks.append(value % 1000)
		value //= 1000
	if not breaks:
		return "zero"
	result = []
	position = len(breaks)
	for x in breaks:
		if x > 99:
			y = x // 100
			result.append(toText.texts[y] + " hundred")
			x %= 100
		if x > 9:
			if 10 <= x <= 19:
				result.append(toText.texts[x])
				x %= 10
			else:
				y = (x // 10) * 10
				result.append(toText.texts[y])
				x %= 10
		if x > 0:
			result.append(toText.texts[x])
		result[-1] = result[-1] + " " + toText.positions[position]
		
	print(result)
	return " ".join(result[::-1])
	
	

print(f"0 = {toText(0)}")	
print(f"5 = {toText(5)}")
print(f"10 = {toText(10)}")
print(f"2,465,187 = {toText(2_465_187)}")
