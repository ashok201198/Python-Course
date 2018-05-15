__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
vowels={'a','e','i','o','u'}
punct={',','.'}
def constranslator(word):
    consonants=''
    flag=0
    if word[0].isupper():
        flag=1
    punc=''
    word = word.lower()
    if word[-1] in punct:
        punc+=word[-1]
        word=word[0:-1]
    for letter in word:
        if letter not in vowels:
            consonants+=letter
        else:
            break
    consonants+="ay"
    word=word[len(consonants)-2:]+consonants+punc
    if flag==1:
        word = word[0].upper() + word[1:]
    return word
def voweltranslator(word):
    flag=0
    if word[0].isupper():
        flag=1
    punc=''
    word=word.lower()
    if word[-1] in punct:
        punc+=word[-1]
        word=word[0:-1]
    word+="ay"+punc
    if flag==1:
        word =word[0].upper()+word[1:]
    return word
def wordformater(words):
    #from string import ascii_letters as letters
    returnlist=[]
    for word in words:
        if word[0].lower() in vowels:
            returnlist.append(voweltranslator(word))
        else:
            returnlist.append(constranslator(word))
    return returnlist
if __name__ == "__main__":
    while True:
        try:
            string=sys.argv[1]
            words=[i for i in string.split()]
            encrypted=wordformater(words)
            print(" ".join(encrypted))
        except KeyboardInterrupt:
            exit()