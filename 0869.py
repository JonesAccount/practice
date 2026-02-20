from random import choice

words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "pot", "top", "opt"]

result = []
lst_find = []
lst_word = []

def find(one_word):
    for index_word in range(len(one_word)):
        letter = one_word[index_word]
        lst = one_word.pop(index_word)
        for index in range(len(one_word)):
            res = one_word.insert(index, letter)
            if res in words:
                print(res)
            else:
                res = None
                print(False)
def word():
    for x in words:
        one_word = list(x)
        find(one_word)
    
word()