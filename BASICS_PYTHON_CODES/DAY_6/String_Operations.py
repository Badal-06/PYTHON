str = "hello_badal"

# To check string is end with any letter :-
print(str.endswith("l")) # True 
print(str.endswith("lo")) # False 

# To make first letter of string capital :-
print(str.capitalize()) # Hello_badal

# To replace a letter or  word with another :-
print(str.replace("hello","welcome")) # welcome_badal
print(str.replace("a","o")) # hello_bodol

# To find index of any letter or word :-
print(str.find("a")) # 7
print(str.find("badal")) # 6

# To count the occurence of any letter or word :-
print(str.count("a")) # 2
print(str.count("hello")) # 1