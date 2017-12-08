def fibonacci(n):
	if n < 0:
		print("Negative no not allowed")

	if n == 0 or n == 1:
		return n

	else:
		return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
	n = int(input("Enter a number"))
	for i in range(0,n+1):
		print(fibonacci(i))