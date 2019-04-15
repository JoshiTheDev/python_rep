#crypto group order script
#author: Joshua Helms
#date: 03.04.2019

#needs to be prime for multiplication as group operation
n = int(input("Group index: "))


def find_orders():

	orders = []
	for i in range(1, n - 1): #range to n-1 to cut out max group order(n-1)
		if((n - 1) % i ==  0): 
			orders.append(i)	
	return orders[::-1] #return reversed (high to low)



def test_element(x,orders):

	generator = True

	#while loop to actively remove items from list
	i = 0
	while i < len(orders):
		
		if(x ** orders[0] % n == 1): #check if valid order
			print("Order {} of element not maximum so element is not a valid generator".format(orders[0]))
			generator = False
			return generator
		else:
			print("Order {} and its factors not valid. Checking following next:".format(orders[0]))
			print(orders)
			orders = [item for item in orders if orders[0] % item != 0]
			print(orders)

		i += 1

	print("Element is of maximum order: valid generator")
	return generator




print("Possible orders for " + str(n) + ": ", end = "")
print(find_orders())
x = int(input("Test element: "))
test_element(x,find_orders())