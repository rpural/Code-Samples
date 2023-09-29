'''
** PYTHON CODE CHALLENGE - PLOT AREAS **
# a tropical paradise realtor has landplots below for sale
# ['ID', length, width] in multiples of 10 m (5 = 50m)
# write code to help them sort list by plot area
plots = (['A',3,3], ['B' ,5,2], ['C', 6,6], ['D', 4,8], ['E' ,11,2]]
#output
"Plots in descending order:
C(6,6), D(4,8), E(11,2), B(5,2), A(3,3)
'''

#plots = [['A',3,3], ['B',5,2], ['C',6,6], ['D',4,8], ['E',11,2]]

plots = [['A',3,3], ['B',5,2], ['C',6,6], ['D',4,8], ['E',11,2]]

def acres(a):
	return a[1] * a[2]
	
print(f"{plots}")
splots = sorted(plots, key=acres, reverse=True)
print(f"{splots}")
