# Check if two words are anagrams 
# Example:
# find_anagram("hello", "check") --> False
# find_anagram("below", "elbow") --> True

#CASE1........Manipulating Strings
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word,anagram=word.lower(),anagram.lower()
    word_split=[]
    for i in word:
        word_split.append(i)
    if len(word)==len(anagram):
        for i in anagram:
            if i in word_split:
                continue
            else:
                return False
    else:
        return False

    return True

#CASE2.........Using sorted option
def find_anagrams(word,anagram):
    word,anagram=word.lower(),anagram.lower()
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False
