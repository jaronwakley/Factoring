# Given a number, this program divides it into two until it is odd and then factors it into two of its factors that are closest to the square root of the number.
# Every number can be expressed as the difference of two square numbers and the factors of the number can be found by taking the square root of those two squares.
# Example: 33 = 7² - 4² | The factors are 7 - 4 and 7 + 4

import math, time

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

num_str = "0"
while 1:
	num_str = input("What number would you like to factor? Press -1 to quit.")
	t1 = time.time()
	if num_str == "-1":
		break
	num = int(num_str)
	number_of_twos = 0
	while num % 2 == 0:
		num = num / 2
		number_of_twos += 1
	n = int(math.sqrt(num))
	if n**2 == num:
		string_to_print = ""
		while number_of_twos > 0:
			string_to_print = string_to_print + "2 "
			number_of_twos -= 1
		if n != 1:
			string_to_print = string_to_print + str(n) + " " + str(n)
		print(string_to_print)
	else:
		num = int(num)
		square = n**2
		difference = square - num
		while 1:
			if difference < 0:
				difference = difference + ((2 * n) + 1)
				n += 1
				continue
			if is_square(difference) == True: #It is square
				string_to_print = ""
				while number_of_twos > 0:
					string_to_print = string_to_print + "2 "
					number_of_twos -= 1
				sqrt = math.sqrt(difference)
				if n - sqrt != 1:
					string_to_print = string_to_print + str(int(n - sqrt)) + " " + str(int(n + sqrt))
				else:
					string_to_print = string_to_print + str(int(n + sqrt))
				t2 = time.time()
				print(string_to_print)
				print("time: " + str(t2 - t1))
				break
			difference = difference + ((2 * n) + 1)
			n += 1