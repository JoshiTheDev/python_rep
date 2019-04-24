#! /bin/python3
#----------------------------------------------------------------------------------------------------------------------------------------------------
#Square and Multiplay algorithm script
#author: Joshua Helms
#date: 03.04.2019

import argparse

#Helper to get a binary list representation
def to_bit_list(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]



if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Square-Multiply algorithm')
	parser.add_argument("-l", "--latex", help="Print output in LaTeX", action='store_true')
	args = parser.parse_args()

	end = ' \\' + '\\'


	base = int(input("Base: "))
	result = base
	exponent = int(input("Exponent: "))
	bin_expo = to_bit_list(exponent)
	modulo = int(input("Modulo: "))

	print(str(base) + '^' + str(exponent) + " mod " + str(modulo))

	#Strip first bit
	bin_expo = bin_expo[1:] 

	#Where the magic happens
	for var in bin_expo:
		if int(var) == 0:
			if(args.latex):
				print("0\quad[SQR]: $" + str(result) + "^2$ mod " + str(modulo), end="")
			else:
				print("0	[SQR]: " + str(result) + "² mod " + str(modulo), end="")

			result = (result * result) % modulo
			
			if(args.latex):
				print(" = " + str(result) + end)
			else:
				print(" = " + str(result))
		else:
			if(args.latex):
				print("0\quad[SQR]: $" + str(result) + "^2$ mod " + str(modulo), end="")
			else:
				print("0	[SQR]: " + str(result) + "² mod " + str(modulo), end="")

			result = (result * result) % modulo
			
			if(args.latex):
				print(" = " + str(result) + end)
			else:
				print(" = " + str(result))
			
			if(args.latex):
				print("1\quad[MUL]: $" + str(result) + " * " + str(base) + "$ mod " + str(modulo), end="")
			else:
				print("1	[MUL]: " + str(result) + " * " + str(base) + " mod " + str(modulo), end="")

			result = (result * base) % modulo

			if(args.latex):
				print(" = " + str(result) + end)
			else:
				print(" = " + str(result))

	print("\nFinal Result: " + str(result))



