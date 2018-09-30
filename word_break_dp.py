def wordBreak(d, word):
	dp = [[0 for col in range(len(word))] for row in range(len(word))] 
	for row in dp:
		print(row)

	for length in range(1, len(word) + 1):
		for j in range(0, length - 1):
			if dp[0][j] and dp[j + 1][length - 1] == True:
				dp[]

if __name__ == "__main__":
	d = ['i', 'am', 'the', 'boss']
	word = "iamtheboss"
	wordBreak(d, word)




# def word_break(s, word_dict):
#     """
#     :type s: str
#     :type word_dict: Set[str]
#     :rtype: bool
#     """
#     dp = [False] * (len(s)+1)
#     dp[0] = True
#     print(dp)
#     for i in range(1, len(s)+1):
#         for j in range(0, i):
#             if dp[j] and s[j:i] in word_dict:
#                 dp[i] = True
#                 break
#     return dp[-1]
  
# if __name__ == "__main__":
#     s = "iamtheboss"
#     dic = ['i', 'am', 'the', 'boss']
 
#     print(word_break(s, dic))