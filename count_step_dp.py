def countStep(dist):

	count = [0 for x in range(0,dist + 1)]

	count[0] = 1
	count[1] = 1
	count[2] = 2

	for i in range (3, dist + 1):
		count[i] = count[i - 1] + count[i - 2] + count[i - 3]

	return count[dist]

if __name__ == "__main__":
	dist = 3
	print(countStep(dist))
