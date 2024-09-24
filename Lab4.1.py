# Find the number of palindrome words in the given sentence without defining any new function (feel free to use 
# python’s in-built functions)

sentence = str(input(""))
palindromes = [word for word in sentence.split() if word.lower() == word.lower()[::-1]]
print(f"\nNumber of palindrome words: {len(palindromes)}")
