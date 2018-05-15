__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys


if __name__ == "__main__":
    from collections import Counter as c
    filename=sys.argv[1]
    f=open(filename,"r")
    words=[]
    for i in f.readlines():
        i=i.lstrip()
        #print(i)
        if i=='':
            continue
        if i[0]!='#' and i[0]!='\n':
            words.append(i.strip('\n'))
    anagram_lists=[]
    processed=[]
    for i in range(len(words)):
        word=words[i]
        if word in processed:
            continue
        list=[]
        word_counter=c(word.lower())
        list.append(word)
        processed.append(word)
        for j in range(i+1,len(words)):
            check_counter=c(words[j].lower())
            if word_counter==check_counter:
                list.append(words[j])
                processed.append(words[j])
        if len(list)>0:
            list.sort(key=lambda x:x.lower())
            anagram_lists.append(list)
    anagram_lists.sort(key=lambda x:x[0].lower())
    anagram_lists.sort(key=len,reverse=True)
    output=filename[:-4]+"-results.txt"
    f.close()
    f=open(output,"w")
    string = ""
    for i in anagram_lists:
        string += "\n".join(i)
        string += "\n"
    f.write(string)
    print(anagram_lists)
    print(string)
    f.close()




