import time
def fibonacci(n):
	if n < 0 :
		print("Negative no not allowed")

	elif n == 0:
		print(0)

	elif n == 1:
		print("0 1")

	else:

		a , b = 0, 1
		for i in range(0,n+1):

			if i == 0 or i == 1 :
				print(i)

			else:

				c = a + b
				a = b
				b = c
			
				print(c)

if __name__ == "__main__":
	n = int(input("Enter a number "))
	start_time = time.time()
	fibonacci(n)
	print("--- %s seconds ---" % (time.time() - start_time))

# 5000 --- 4.88319587708 seconds ---
# 10000 --- 19.5836691856 seconds ---

# def fibonacci(n):
# 	if n < 0 :
# 		print("Negative no not allowed")

# 	elif n == 0:
# 		return 0

# 	elif n == 1:
# 		return 1

# 	else:

# 		a , b = 0, 1
# 		for i in range(0,n+1):

# 			if i == 0 or i == 1 :
# 				pass

# 			else:

# 				c = a + b
# 				a = b
# 				b = c
			
# 		return c

# if __name__ == "__main__":
# 	n = int(input("Enter a number "))
# 	start_time = time.time()
# 	for i in range(0,n+1):
# 		print(fibonacci(i))
# 	print("--- %s seconds ---" % (time.time() - start_time))


# 5000 --- 4.93998217583 seconds ---
# 10000 --- 19.6891801357 seconds ---


