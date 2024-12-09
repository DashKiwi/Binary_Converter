import os

def int_checker(message, allowed, base, max = -1):
	while True:
		try:
			number = input(message).upper()
			if max > 0 and len(number) > max:
				raise
			if "#" in number[0] and base == "Hex color code":
				number = number[1:]
			if number != "" and number != "E":
				for i in number:
					if i not in allowed:
						raise
			if base == "Red RGB code (0-255)" or base == "Green RGB code (0-255)" or base == "Blue RGB code (0-255)":
				if not (0 <= int(number) <= 255):
					raise
			return number
		except:
			print(f"Please enter a valid {base}\n")

def two_to_ten():
	while True:
		print("~~~~ Base 2 to Base 10 ~~~~\n\nEnter E to return to main menu")
		base2 = int_checker("Please enter a base-2 number:\n>> ", ["0", "1"], "Base-2 number")
		if base2 == "E":
			break
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
		bit_length = int_checker("Please input the bit computing size or blank for program to find (max 512 bits):\n>> ", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""], "Base-10 number")
		shorten = False
		if bit_length == "E":
			break
		elif bit_length == "":
			bit_number = 512
			shorten = True
		elif int(bit_length) > 512:
			print("Bit number to large! Defaulting to 512 bits")
			bit_number = 512
		else:
			bit_number = int(bit_length)
		byte = []
		base10 = int(int_checker("\nPlease enter a base-10 integer number:\n>> ", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], "Base-10 number"))
		if base10 == "E":
			break
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

def hex_to_rgb():
	allowed_inputs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	while True:
		try:
			print("~~~~ Hex to RGB ~~~~\n\nEnter E to return to main menu")
			hex_code = int_checker("Please input the hex code to convert to RGB\n#", allowed_inputs, "Hex color code")
			if hex_code == "E":
				break
			hex_code_lst = list(hex_code)
			hex_code_lst = list(reversed(hex_code_lst))
			if len(hex_code_lst) != 3 and len(hex_code_lst) != 6:
				raise
			j = 1
			while len(hex_code_lst) < 6:
				hex_code_lst.insert(j, allowed_inputs[allowed_inputs.index(str(hex_code_lst[j - 1]))])
				j += 2
			r = g = b = 0
			for i in range(len(hex_code_lst)):
				if i >= 4 and i <= 5:
					r += (16 ** (i - 4)) * allowed_inputs.index(str(hex_code_lst[i]))
				elif i >= 2 and i <= 3:
					g += (16 ** (i - 2)) * allowed_inputs.index(str(hex_code_lst[i]))
				elif i >= 0 and i <= 1:
					b += (16 ** i) * allowed_inputs.index(str(hex_code_lst[i]))
				else:
					break
			os.system("cls||clear")
			print(f"~~~~ RESULT ~~~~\nThe RGB color code for hex #{hex_code} is {r, g, b}\n~~~~~~~~~~~~~~~~\n")
		except:
			os.system("cls||clear")
			print("Please enter a 3 or 6 digit Hex color code to convert into RGB color code")

def rgb_to_hex():
    allowed_inputs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        try:
            print("~~~~ RGB to Hex ~~~~\n\nEnter E to return to main menu")
            r_code = int_checker("Please input the Red RGB code (0-255): ", allowed_inputs, "Red RGB code (0-255)", 3)
            if r_code == "E":
                break
            g_code = int_checker("Green: ", allowed_inputs, "Green RGB code (0-255)", 3)
            if g_code == "E":
                break
            b_code = int_checker("Blue: ", allowed_inputs, "Blue RGB code (0-255)", 3)
            if b_code == "E":
                break
            r_code = int(r_code)
            g_code = int(g_code)
            b_code = int(b_code)
            hex_r = format(r_code, '02X')
            hex_g = format(g_code, '02X')
            hex_b = format(b_code, '02X')
            hex_value = f"#{hex_r}{hex_g}{hex_b}"
            os.system("cls||clear")
            print(f"~~~~ RESULT ~~~~\nThe Hex color code for RGB({r_code}, {g_code}, {b_code}) is {hex_value}\n~~~~~~~~~~~~~~~~\n")
        except:
            os.system("cls||clear")
            print(f"Please enter valid RGB values between 0 and 255.")

def main_menu():
	while True:
		os.system("cls||clear")
		print("~~~~ Binary Converter by DashKiwi ~~~~\n")
		choice = input("Please enter a corresponding number:\n\n1. Base-10 to Base-2\n2. Base-2 to Base-10\n3. Hex to RGB\n4. RGB to Hex\n5. Exit\n\n>> ")
		if choice == "1":
			os.system("cls||clear")
			ten_to_two()
		elif choice == "2":
			os.system("cls||clear")
			two_to_ten()
		elif choice == "3":
			os.system("cls||clear")
			hex_to_rgb()
		elif choice == "4":
			os.system("cls||clear")
			rgb_to_hex()
		elif choice == "5":
			print("Thank you for using DashKiwi's Converter. Have a good day!")
			quit()
		else:
			os.system("cls||clear")
			print("Please enter a valid Base-10 number (1-3)\n")

main_menu()
