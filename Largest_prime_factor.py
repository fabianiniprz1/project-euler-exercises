#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def Largest_prime_factor(num):
	
	for pf in range(num + 1):
		
		if pf == 0:
			continue

		if num % pf == 0:
			lpf = pf
			num = num / pf

		if num == 1:
			break				

	return lpf

		
		
	

def start_lpf():
	num = int(input('Enter a number to know what is its largest prime factor: '))
	print(Largest_prime_factor(num))
	