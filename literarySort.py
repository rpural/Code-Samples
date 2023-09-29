'''
🐍 PYTHON CODE CHALLENGE - SPECIAL SEATING

# you're planning a dinner for a special literary society, and seating arrangement is very particular. Create a Python function: sort_names, sorting list of names first by length of name and then alphabetically.  This way, everyone can find their seats with ease!

names = ["Ava", "Ella", "Emma", "Liam", "Lucas", "Mia", "Noah", "Oliver", "Sophia", "William"]

def sort_names(names):

# Your code here

pass

# Test your function to ensure it correctly sorts the names

sorted_names = sort_names(names)

print(sorted_names)

# Bonus:

# modify function to make sure the chairman and founder, Oliver comes last.

Please share your code in a format that is easy for others to copy and test 👍

Have fun
'''

names = ["Ava", "Ella", "Emma", "Liam", "Lucas", "Mia", "Noah", "Oliver", "Sophia", "William"]

def sort_names(names):
	sort_list = [(len(x), x) for x in names if x != "Oliver"]
	result_list = sorted(sort_list, key=lambda x: f"{x[0]:02d} {x}")
	if "Oliver" in names:
		result_list.append((0,"Oliver"))
	return [x[1] for x in result_list]


if __name__ == "__main__":
	sorted_names = sort_names(names)

	print(sorted_names)
