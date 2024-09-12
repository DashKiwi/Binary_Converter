import os

def int_checker(message, allowed, base):
	while True:
		try:
			number = input(message).capitalize()
			if number != "" and number != "E":
				for i in number:
					if i not in allowed:
						raise
			return number
		except:
			print(f"Please enter a valid {base} number\n")

def two_to_ten():
	while True:
		print("~~~~ Base 2 to Base 10 ~~~~\n\nEnter E to return to main menu")
		base2 = int_checker("Please enter a base-2 number:\n>> ", ["0", "1"], "Base-2")
		if base2 == "E":
			main_menu()
		base2_array = []
		for i in base2[::-1]:
			base2_array.append(i)
		counter = 1
		integer = 0
		for i in base2_array:
			if i == "1":
				integer += counter
			counter = counter * 2
		os.system("cls||clear")
		print(f"~~~~ RESULT ~~~~\nThe base-10 number for base-2 {base2} is {integer}\n~~~~~~~~~~~~~~~~\n")

def ten_to_two():
	while True:
		print("~~~~ Base 10 to Base 2 ~~~~\n\nEnter E to return to main menu")
		bit_length = int_checker("Please input the bit computing size or blank for program to find (max 512 bits):\n>> ", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""], "Base-10")
		shorten = False
		if bit_length == "E":
			main_menu()
		elif bit_length == "":
			bit_number = 512
			shorten = True
		elif int(bit_length) > 512:
			print("Bit number to large! Defaulting to 512 bits")
			bit_number = 512
		else:
			bit_number = int(bit_length)
		byte = []
		base10 = int(int_checker("\nPlease enter a base-10 integer number:\n>> ", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], "Base-10"))
		if base10 == "E":
			main_menu()
		integer = base10
		binary = ""
		place_value = pow(2, bit_number - 1)
		for i in range(bit_number):
			byte.append(False)
			if integer >= place_value:
				byte[i] = True
				integer -= place_value
			place_value = place_value / 2
		for i in byte:
			if not i:
				binary += "0"
				if binary == "0" and shorten == True:
					binary = ""
			else:
				binary += "1"
		extra_message = ""
		if integer > 0:
			extra_message = f"BEWARE The number you have entered exceeds the {bit_number} bit limit\nThis means that it will return a series of 1's\n"
		os.system("cls||clear")
		print(f"~~~~ RESULT ~~~~\n{extra_message}The base-2 number for base-10 {base10} is {binary}\n~~~~~~~~~~~~~~~~\n")

def main_menu():
	os.system("cls||clear")
	while True:
		print("~~~~ Binary Converter by DashKiwi ~~~~\n")
		choice = input("Please enter a corresponding number:\n\n1. Base-10 to Base-2\n2. Base-2 to Base-10\n3. Exit\n\n>> ")
		if choice == "1":
			os.system("cls||clear")
			ten_to_two()
		elif choice == "2":
			os.system("cls||clear")
			two_to_ten()
		elif choice == "3":
			quit()
		else:
			os.system("cls||clear")
			print("Please enter a valid Base-10 number (1-3)\n")

main_menu()
