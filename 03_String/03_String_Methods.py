'''String Methods:-'''

# Common String Methods

'''upper()'''

# It converts all characters into uppercase.

# Example:-

my_string = "Python is a Programming Language"
print("before any operation:", my_string)

print("after any operation:", my_string.upper())
# ___________________________________________________

# Example:-

'''lower()'''
# ⇒ It converts all characters into lowercase.

my_string = "Python is a Programming Language"
print("before any operation:", my_string)

print("after any operation:", my_string.lower())
# ___________________________________________________

'''capitalize()'''

# ⇒ It converts the first character of the first word into uppercase.

# Example:-

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.capitalize())

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.capitalize())

# ___________________________________________________

'''title()'''

# ⇒ It converts the first character of each word in a sentence.

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.title())
# ___________________________________________________

'''strip()'''

# ⇒ It removes extra spaces.

# Example:-
my_string = "             python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.strip())
# ___________________________________________________

'''replace()'''
# ⇒ It replaces a word or character with another word or character.

# Example:-

my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.replace("python", "Java"))

# ___________________________________________________
'''split()'''

# ⇒ It splits a string into a list.

# Example:-
my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.split())

# ___________________________________________________

'''find()'''
# ⇒ Finds the first occurrence position of a character or word.

# Example:-

my_string = "Programming"
print("before any operation:", my_string)

print("after any operation:", my_string.find("P"))
print("after any operation:", my_string.find("m"))

# ___________________________________________________

'''startswith()'''
# ⇒ Check if the string starts with a specific word.

# Example:-
my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.startswith("Programming")) # False 
print("after any operation:", my_string.startswith("python")) # True

# ___________________________________________________
'''endswith()'''

# ⇒ Check if the string ends with a specific word

# Example:-
my_string = "python is a programming language"
print("before any operation:", my_string)

print("after any operation:", my_string.endswith("Language")) # False 
print("after any operation:", my_string.endswith("language")) # True

# ___________________________________________________

'''index()'''
# ⇒ Find the position of a substring or any character.

# Example:-
print("before any operation:", my_string) 

print("after any operation:", my_string.index("m")) # 6 , similar to find() method

# ___________________________________________________

'''count()'''
# ⇒ Count how many times a character or word appears in a string.

# Example:-
my_string = "programming"
print("before any operation:", my_string) 

print("after any operation:", my_string.count("m")) # 2

# ___________________________________________________
