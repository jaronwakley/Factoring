# Given a number this program factors it into two of its factors.
# Every number that is not 2ⁿ can be expressed as the difference of two triangle numbers.
# With this the two factors of that number can be found


import time

while 1:
	number = input("What number would you like to factor? Press -1 to quit.")
	if number == "-1":
		break
	number = int(number)
	top_number = 0
	bottom_number = 1
	total = 0
	t1 = time.time()
	while total != number:
		while total < number:
			top_number += 1
			total += top_number
		while total > number:
			total -= bottom_number
			bottom_number += 1
	#print(bottom_number)
	#print(top_number)
	if bottom_number % 2 == 1:
		if top_number % 2 == 0:
			factor = bottom_number + top_number
			print("factors: " + str(int(total / factor)) + " " + str(factor))
		else:
			factor = int((bottom_number + top_number) / 2)
			print("factors: " + str(factor) + " " + str(int(total / factor)))
	else:
		if top_number % 2 == 0:
			factor = int((bottom_number + top_number) / 2)
			print("factors: " + str(factor) + " " + str(int(total / factor)))
		else:
			factor = bottom_number + top_number
			print("factors: " + str(int(total / factor)) + " " + str(factor))
	t2 = time.time()
	print("time: " + str(t2 - t1))