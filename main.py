number = int(input('Enter the base: '))
exponent = int(input('Enter the exponent: '))
result = str(number ** exponent)
count = 0
acum = 0

while (len(result) > count):
	acum += int(result[count])
	print(acum)
	count	+= 1


print (acum)
