word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1) == sorted(word2):
    print("Words are Anagram")
else:
    print("Words are Not Anagram")