__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(text, n):
    if text==None or n==None:
        return None
    if n<=0:
        raise ValueError
    if type(text).__name__!="str":
        raise TypeError
    list1 = [[] for _ in range(n)]
    text2 = list(text)
    if n == 1:
        return text
    list1 = [[] for _ in range(n)]
    text2 = list(text)
    if n == 1:
        return text
    flag = 1  # 0-for going up and 1-for going down
    k = n
    while True:
        if k == -1:
            k = 0
            flag = 0
        elif k == n:
            k = n - 1
            flag = 1
        if len(text) - k > 0:
            list1[k].append(text[0:k + 1])
        else:
            list1[k].append(text[:])
            break
        text = text[k + 1:]
        if flag:
            k -= 1
        else:
            k += 1
    list2 = [i for j in range(len(list1)) for i in list1[j]]
    return ("".join(list2))
def test_unjumble():
    #assert "Ashokan" == unjumble("hoAskan", 2)
    #print(unjumble("hoAskan", 2))
    print(unjumble(" t iuswhpphihere am ing atsa!",2))