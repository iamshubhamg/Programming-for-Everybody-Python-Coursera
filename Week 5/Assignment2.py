hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
