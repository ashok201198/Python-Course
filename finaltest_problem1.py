__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''

def repeats(digits):
    if digits==None:
        return None
    if type(digits).__name__!="str":
        raise TypeError
    list1=[]
    list2=[]
    for i in range(len(digits)-1):
        for j in range(i+1,len(digits)):
            if digits[i:j] not in list1:
                k=digits.count(digits[i:j])
                if k>=2 and len(digits[i:j])>=2:
                    list1.append(digits[i:j])
                    list2.append(k)
    result=[(list1[i],list2[j]) for i in range(len(list1)) for j in range(len(list2)) if i==j ]
    result.sort(key=lambda x:int(x[0]), reverse=True)
    result.sort(key=lambda x:x[1],reverse=True)
    return result
def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")
    print(repeats("1"))