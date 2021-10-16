# -*- coding: utf-8 -*-
"""
CCT MSc DA -- Programming Python (Amilcar Aponte amilcar@cct.ie)
@author: Lajos Reisenleitner sba-21-727

Calculator v1.3

"""
import numpy # for round(complex) only

class Calculator:
	'''Basic Arithmetic Calculator
		A - Addition
		S - Subtraction
		P - Product
		D - Division
		E - Exponential
		R - Root
		M - Modulus
		C - Close the program
	'''

	op_str = "ASPDERMC"
	menu_str = {'A':"Addition",'S':"Subtraction",'P':"Product",'D':"Division",'E':"Exponential",'R':"Root",'M':"Modulus",'C':"Close the program"}
	menu_str2 = ["only two inputs","of n numbers"]
	msg = {"C_ON":"The Calculator is running...","C_OFF":"...The Calculator has stopped.",
		"MT":"------ Operation menu ------","CH":"Please choose!",
		"N":"How many numbers would you like to type in? ", "F":"Give the number", "X":" (X:finish)",
		"ERR_N":"You need to give an integer number between 2 and 20.", "ERR_F":"You need to give a number",
		"ERR_OP":"Not enough input ::: ", "ERR_VAL":"Value Error", "ERR_ZDIV":"Zero Division Error"}

	def on(self):
		"""Start the running"""
		print("\n"+self.msg["C_ON"])
		self.main()

	def off(self):
		"""Close the running"""
		print("\n"+self.msg["C_OFF"])

	def menu(self):
		''' Prints the menu '''

		print("\n\t"+self.msg["MT"]+"\n")

		for s in self.op_str:
			s_ = "\t "+s+" - "+self.menu_str[s]

			if s == 'C':
				print("\n"+s_)
			else:
				print(s_+" ("+self.menu_str2[s in "AP"]+")")

	def operation(self,op):
		"""Operations - the hearth of the calculation"""

		o_ = {'A':"+",'S':"-",'P':"*",'D':"/",'E':"**",'R':"V‾",'M':"%",'C':""}
		n = 2
		nums = []
		print("\n\t <====== "+self.menu_str[op].upper()+" ======>")


	# n=?
		if op in "AP":
			while True:
				try:
					n = int (input(self.msg["N"]+" > ").strip())
					if 2<=n<=20: break
				except: pass
				print(self.msg["ERR_N"])

	# n1, n2... =?
		isX = False
		print("\t\t\t\t\t\t"+self.msg["X"])
		for i in range(0, n):

			while True:
				try:
					f = input(self.msg["F"]+" "+str(i+1)+"#"+str(n)+" > ").strip()
					if f in "xX" and f:
						isX = True
						break
					f = float(f)
					if f== -0.0: f=0.0
				except:
					print(self.msg["ERR_F"])
					continue			
				nums.append(f)
				break
			# ..while
			if isX: break
		#..for

	# operations
		n = len(nums)
		result_str=""
		if n<2: print(self.msg["ERR_OP"])
		else:
			f = nums.pop(0)
			result_str = str(f)
			result = f

			try:
				for i in range(0, n-1):
					f = nums.pop(0)
					if op=='R': result_str = str(f)+o_[op]+" "+result_str
					else: result_str += " "+o_[op]+" "+str(f)

					if   op=='A': result += f
					elif op=='S': result -= f
					elif op=='P': result *= f
					elif op=='D': result /= f
					elif op in "ER":
						if op=='E': result **= f
						else: result **= (1/f)
						if type(result) == float: result=round(result, 8)
						elif type(result) == complex: result=numpy.around(result, 8)
					elif op=='M': result %= f

				result_str += " = "+str(result)
				print(result_str)
				print("\n"+str(result))
			except: print(self.msg["ERR_ZDIV"])
				
	def main(self):
		"""Main program"""

		self.menu()
		while True:

			op = input(self.msg["CH"]+" > ").strip().upper()
			if len(op) != 1 or op not in self.op_str:
				print(self.msg["ERR_OP"]+op)
				continue
			elif op == "C": break
			
			self.operation(op)

			self.menu()

		self.off()
#==============================================================================

# Create object
calculator = Calculator()

# Running...
calculator.on()