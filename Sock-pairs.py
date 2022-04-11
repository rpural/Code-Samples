''' ** PYTHON CODE CHALLENGE - SORTING SOCKS **
# after doing your laundry, you now have a bag full of socks
# to pair up and sort. right and left socks are mirror images
# of each other so 'ad' is paired with 'da', 'pl' with '1p
etc.
# write code to pair and sort your socks, putting
# leftover singles in a separate 'bag' for next time.
'''

socks = [ 'lv','eb','ho', 'ug', 
			'da', 'be', 'se', 'kc',
			'p1', 'ck', 'gu', 'vl', 'nb', 'ad' ]

''' # your output should be
pairs
= [['ad', 'da'], ['be', 'eb'], ['ck', 'kc'], 
	['gu', 'ug'], ['lv', 'vl']]
singles = ['nb', 'pl', 'ho', 'se'] '''

socks.sort()

pairs = []
singles = []

while socks:
	left = socks.pop()
	found = False
	for i, right in enumerate(socks):
		if left[::-1] == right:
			pairs.append([left, right])
			socks.pop(i)
			found = True
			break
	if not found:
		singles.append(left)

print(pairs)
print(singles)
