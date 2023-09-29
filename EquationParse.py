'''
This was a fun little task from another group. Write a function to compute these expressions, without using exec/eval. You may assume the strings contain only integers and the 4 basic operators, + - * / 



You may assume that each string holds a valid expression.
'''

import re

explist = ["4 + 5 - 2 * 3 + 6 + 4*3 - 8 / 2",
	"18 + 67 / 4 - 80 * 155", "15 + 78 * 178 - 90",
	"157*45-78/88", 
	"4 + 4 * 2 / ( 1 - 5 )",
	"4.5 - .75 + 2.25 * 4",
]

def parse_equation(equ : str):
	''' Accept an expression in infix notation
	    and convert it to postfix notation so
	    that it can be easily evaluated.
	
	    Operations supported are:
	        +, -, *, /, and ()
	
	    input: a text sring containing the
	           equation to be evaluated. It is
	           assumed that the equation is
	           syntactly correct, and in
	           infix notation.
	
	    output: a list containing the postfix
	            equation, broken down into
	            individual tokens.
	'''
	pres = {"+":  5, "-":  5,
	        "*": 10, "/": 10,
	        "^": 15,
	        "(": -1, ")": -1, }
	
	output = []
	stack = []
	state = "operand"
	
	input = re.findall(r'[.0-9]+|\D',
	                 equ.replace(" ",""),
	                 re.ASCII)
	
	while input:
		atom = input.pop(0)
		if atom not in pres:
			output.append(atom)
		else:
			if len(stack) == 0:
				stack.append(atom)
			else:
				if atom == "(":
					stack.append(atom)
				elif atom == ")":
					while stack[-1] != "(":
						output.append(stack.pop())
					stack.pop()
				else:
					while len(stack) > 0 and pres[atom] <= pres[stack[-1]]:
						output.append(stack.pop())
					stack.append(atom)
	while len(stack) > 0:
		output.append(stack.pop())
	return output

	
def process_postfix(equ : list):
	''' Given a list of tokens in postfix
	    order, return the result of the
	    equation.
	
	    input: a list containing an 
	           equation in postfix order.
	
	    output: the float result of 
	            evaluating the equation.
	'''
	operation = {"+": float.__add__,
	             "-": float.__sub__,
	             "*": float.__mul__,
	             "/": float.__truediv__, }
	stack = []
	while len(equ) > 0:
		atom = equ.pop(0)
		if re.match(r"[.0-9]+", atom):
			stack.append(atom)
		else:
			x = float(stack.pop())
			y = float(stack.pop())
			stack.append(str(operation[atom](y, x)))
	return stack.pop()
			
	
if __name__ == "__main__":
	for e in explist:
		''' show the equation to be evaluated,
		    show the result of passing it
		    to eval, then show the result of
		    calling parse_equation() and
		    process_postfix().
		'''
		print(e)
		print("eval = ", eval(e))
		postfix = parse_equation(e)
		result = process_postfix(postfix)
		print("=", result)
		print()
