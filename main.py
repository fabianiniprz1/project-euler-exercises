from Power_digit_sum import *
from Multiples_of_3_and_5 import *
from Largest_prime_factor import *

def main():

	x = int(input('select the problem: '))
	
	if x == 1:
		call_M_3_5()
	elif x == 3:
		start_lpf()
	elif x == 16:
		Power_digit_sum()

if __name__ == '__main__':
    main()