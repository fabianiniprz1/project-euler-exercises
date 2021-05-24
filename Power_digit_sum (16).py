#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?

def Power_digit_sum():
	number = int(input('Enter the base: '))
	exponent = int(input('Enter the exponent: '))
	result = str(number ** exponent)
	count = 0
	acum = 0

	while (len(result) > count):
		acum += int(result[count])
		count	+= 1

	print (acum)
