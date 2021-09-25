# math conjanction

def findeIter(num):
	iter = 0
	while num != 1:
		if num % 2 != 0:
			num = num * 3 + 1
			iter += 1
		else:
			num = num / 2
			iter += 1
	print (iter)

x = 2#int(input("Enter a number: "))

for i in range (100000):
	findeIter(x)
	x += 1