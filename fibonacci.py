"""
	Author: Durga Nula
	Date: July 23rd 2023
	
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""


def fibonacci(n):
	if n == 1 or n == 0:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n - 1)


number = int(input("Enter the number: "))

if number < 0:
	print("Number is not valid")

i = 0

for i in range(0, number):
	print(fibonacci(i))
