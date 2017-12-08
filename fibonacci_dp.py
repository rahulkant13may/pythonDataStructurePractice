def fibonacci(n):
	if n < 0 :
		print("Negative no not allowed")

	if n == 0 or n == 1 :
		print(n)

	a , b = 0, 1
	for i in range(0,n):

		if i == 0 or i == 1 :
			print(i)

		else:

			c = a + b
			a = b
			b = c
		
			print(c)

if __name__ == "__main__":
	n = int(input("Enter a number "))
	fibonacci(n)

