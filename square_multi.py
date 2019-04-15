#Square and Multiplay algorithm script
#author: Joshua Helms
#date: 03.04.2019


#Helper to get a binary list representation
def to_bit_list(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]


base = int(input("Base: "))
result = base;
exponent = int(input("Exponent: "))
bin_expo = to_bit_list(exponent)
modulo = int(input("Modulo: "))

print(str(base) + '^' + str(exponent) + " mod " + str(modulo))

#Strip first bit
bin_expo = bin_expo[1:] 

#Where the magic happens
ctr = 1
for var in bin_expo:
	if int(var) == 0:
		print("0	[SQR]: " + str(result) + "² mod " + str(modulo), end="")
		result = (result * result) % modulo
		ctr *= 2
		print(" = " + str(result) + '\t' + str(ctr))
	else:
		print("-	[SQR]: " + str(result) + "² mod " + str(modulo), end="")
		result = (result * result) % modulo
		ctr *= 2
		print(" = " + str(result) + '\t' + str(ctr))
		print("1	[MUL]: " + str(result) + " * " + str(base) + " mod " + str(modulo), end="")
		result = (result * base) % modulo
		ctr += 1
		print(" = " + str(result) + '\t' + str(ctr))

print("\nFinal Result: " + str(result))



