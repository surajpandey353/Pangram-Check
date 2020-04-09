# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def check_pangram(mystring,alphabets):
    alpha = list(alphabets)
    print(alpha)

    string = mystring.lower()
    list1= list(string)
    string2 = []
    for item in list1:
        if item not in string2:
            string2.append(item)

    string3 = sorted(string2)
    print(string3)
    if string3 == alpha:
        return True
    else:
        return False
print(check_pangram("The quick brown fox jumps over the lazy dog"," abcdefghijklmnopqrstuvwxyz"))




    
    
