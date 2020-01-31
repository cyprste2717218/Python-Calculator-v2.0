print("------------------------")
print("Calculator 2.0")
print("------------------------")
print("Welcome to Calculator 2.0, press enter to continue")
print("")
enter = input("...")

print("")
print("Using the top row of the keyboard, enter the number of the function you want to use:")
print("")
print(" - Standard operations(+-*/) = 1 ")
print(" - Powers of base numbers(²,³..) = 2")
print(" - Compound or simple interest of a base amount = 3")
print(" - Quadratic roots/y-intercept solver = 4")
print(" - Total Cost after additional percentage tax on a list of items = 5")
print("")


def numinput():

	input1 = input("...")

	def again1():
		
		rst1 = input("...")

		if rst1 == "y":
			numinput()
		elif rst1 == "n":
			exit()
		elif rst1 == "info":
			print("")
			print("Using the top row of the keyboard, enter the number of the function you want to use:")
			print("")
			print(" - Standard operations(+-*/) = 1 ")
			print(" - Powers of base numbers(²,³..) = 2")
			print(" - Compound or simple interest of a base amount = 3")
			print(" - Quadratic roots/y-intercept solver = 4")
			print(" - Total Cost after additional percentage tax on a list of items = 5")
			print("")
			numinput()
		else:
			again1()

	def again():

		print("")
		print("Reset?")
		print("Type Y or N into the console")
		print('Hint: Type "info" into the console to bring up the function list if needed')
		rst1 = input("...")

		if rst1 == "y":
			numinput()
		elif rst1 == "n":
			exit()
		elif rst1 == "info":
			print("")
			print("Using the top row of the keyboard, enter the number of the function you want to use:")
			print("")
			print(" - Standard operations(+-*/) = 1 ")
			print(" - Powers of base numbers(²,³..) = 2")
			print(" - Compound or simple interest of a base amount = 3")
			print(" - Quadratic roots/y-intercept solver = 4")
			print(" - Total Cost after additional percentage tax on a list of items = 5")
			print("")
			numinput()
		else:
			again1()

	def func5():
		print("------------------------")
		print("Total Cost after additional percentage tax on a list of items")
		print("------------------------")
		print("")

		print("How many items?")

		numitems = input("")

		if numitems.isdigit() == True:
			again() 



	def func4():
		print("----------------------------")
		print("Quadratic Function Values Finder")
		print("----------------------------")
		print("")
		print("Format ax² + bx + c")

		global numA
		global numB
		global numC

		def roots():
			roots_1 = -1*numB
			roots_2 = (numB ** 2)
			roots_3 = numA*numC
			roots_4 = -4 * roots_3
			roots_5 = roots_2 + roots_4 
			roots_6 = pow(roots_5, 0.5)
			roots_6_1 = roots_1 + roots_6
			roots_6_2 = roots_1 - roots_6
			roots_7_1 = roots_6_1 / (2*numA)
			roots_7_2 = roots_6_2 / (2*numA)

			y1 = numA * (0 ** 2)
			y2 = numB * 0
			y3 = numC
			y4 = y1 + y2 + y3

			print("")
			print("Roots")
			print("")
			root1 = roots_7_1
			print("= ", root1)

			root2 = roots_7_2
			print("= ", root2)

			print("")
			print("Y-intercept")
			print("")
			print("= ", y4)
			
			again()


		def numC1():
			global numC
			numC = input("c = ")

			if numC.isdigit() == True:
				numC = int(numC)
				roots()
			else:
				numC1()

		def numC():
			global numC
			numC = input("c = ")

			if numC.isdigit() == True:
				numC = int(numC)
				roots()
			else:
				numC1()

		
		def numB1():
			global numB
			numB = input("b = ")

			if numB.isdigit() == True:
				numB = int(numB)
				numC()
			else:
				numB1()

		def numB():
			global numB
			numB = input("b = ")

			if numB.isdigit() == True:
				numB = int(numB)
				numC()
			else:
				numB1()

		def numA1():
			global numA
			numA = input("a = ")
		
			if numA.isdigit() == True:
				numA = int(numA)
				numB()
			else:
				numA1()

		def numA():
			global numA
			numA = input("a = ")
			
			if numA.isdigit() == True:
				numA = int(numA)
				numB()
			else:
				numA1()

		numA()

	def func2():

		def pow_bs2():

			def pow_bs2r():

				global pw
				pw = input("...")

				if pw.isdigit() == True:
					pw = int(pw)
					print("Ok, to the power of ", pw)
					final = pow(base, pw)
					print("Answer = ", final)
					
					again()
				else:
					pow_bs2r()


			print("")
			print("Power?")

			global pw
			pw = input("...")

			if pw.isdigit() == True:
				pw = int(pw)
				print("Ok, to the power of ", pw)
				final = pow(base, pw)
				print("Answer = ", final)
				
				again()
				
			else:
				pow_bs2r()

		def pow_bs():
			
			def pow_bs1():

				global base
				base = input("...")


				if base.isdigit() == True:
					base = int(base)
					print("")
					print("Ok, ", base)
					pow_bs2()
				else:
					pow_bs1()


			print("What base number?")
			global base
			base = input("...")


			if base.isdigit() == True:
				base = int(base)
				print("")
				print("Ok, ", base)
				pow_bs2()
			else:
				pow_bs1()

		
		print("------------------------")
		print("Powers of base numbers")
		print("------------------------")
		print("")

		pow_bs()

	def func1():

		print("------------------------")
		print("Standard Operations")
		print("------------------------")
		print("")



		def firstnumcheck():

			def secondnumcheck():
				print("")
				print("Second number?")
				global secondnum
				secondnum = input("...")


				if secondnum.isdigit() == True:
					secondnum = int(secondnum)
					print("")
					print("Ok, ", secondnum)
				

					def operations():
						
						def operations1():

							inp1 = input("...")
							

							if inp1 == "1":
								sum1 = firstnum + secondnum
								print("Answer =", sum1)
								again()
							elif inp1 == "2":
								sub = firstnum - secondnum
								print("Answer =", sub)
								again()
							elif inp1 == "3":
								div = firstnum / secondnum
								print("Answer =", div)
								again()
							elif inp1 == "4":
								mult = firstnum * secondnum
								print("Answer =", mult)
								again()
							else:
								operations1()

						print("")
						print("Which operation?")
						print("Enter the number of the operation you want to use:")
						print("+ = 1")
						print("- = 2")
						print("/ = 3")
						print("x = 4")
						print("")

						inp1 = input("...")
						

						if inp1 == "1":
							sum1 = firstnum + secondnum
							print("Answer =", sum1)
							again()
						elif inp1 == "2":
							sub = firstnum - secondnum
							print("Answer =", sub)
							again()
						elif inp1 == "3":
							div = firstnum / secondnum
							print("Answer =", div)
							again()
						elif inp1 == "4":
							mult = firstnum * secondnum
							print("Answer =", mult)
							again()
						else:
							operations1()

					operations()

				else: 
					secondnumcheck()


			print("First number?")
			global firstnum
			firstnum = input("...")

			if firstnum.isdigit() == True:
				firstnum = int(firstnum)
				print("")
				print("Ok, ", firstnum)
				secondnumcheck()

			else: 
				firstnumcheck()


		firstnumcheck()


	if input1 == "1":
		func1()

	elif input1 == "2":
		func2()
	elif input1 == "3":
		print("In works...")
		numinput()
	elif input1 == "4":
		func4()
	elif input1 == "5":
		print("In works...")
		numinput()
	elif input1 == "info":
		print("")
		print("Using the top row of the keyboard, enter the number of the function you want to use:")
		print("")
		print(" - Standard operations(+-*/) = 1 ")
		print(" - Powers of base numbers(²,³..) = 2")
		print(" - Compound or simple interest of a base amount = 3")
		print(" - Quadratic roots/y-intercept solver = 4")
		print(" - Total Cost after additional percentage tax on a list of items = 5")
		print("")
	else:
		print("Enter the number of a function!")
		numinput()

numinput()



input2 = input("...")