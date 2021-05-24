#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_3_and_5(num):
	account = 1
	accum = 0

	while(account < num):
		if account % 3 == 0 or account % 5 == 0:
			accum += account
		account += 1
	
	print(accum)

def call_M_3_5():
	num = int(input('Enter a number to know what is the accumulated of multiples of 3 and 5: '))
	multiples_3_and_5(num)
