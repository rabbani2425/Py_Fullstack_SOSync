'''List Methods:-'''

# Common List Methods

'''append():-it is used to add a single element at the end of list'''

# Example:-
my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.append(99)
print("After Operation: ", my_list)  # Output = [11,22,33,44,99]
# _______________________________________________________________________________

'''Extend([]):-It is used to add multiple elements at the end of list'''

# Example :- 
my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.extend([99,101,102])
print("After Operation: ", my_list)  #Output = [11,22,33,44,99,101,102]
# _______________________________________________________________________________

'''Insert():-It is used to add an element at specified index'''

# Example :- 
my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.insert(3,102)
print("After Operation: ", my_list) #Output = [11,22,33,102,44]
# _______________________________________________________________________________


'''remove():-Removes a specific element from a list '''

# Example :- 
my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.remove(33)
print("After Operation: ", my_list) # Output =  [11,22,33,]
# _______________________________________________________________________________

'''pop():-By default it removes the last index element'''


# Example :- 

my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.pop()
print("After Operation: ", my_list) #Output =  [11,22,33]

my_list.pop(2)
print("After Operation: ", my_list)  #Output = [11,22,44]
# _______________________________________________________________________________

'''reverse ():-Reverse the order of element in a list''' 

# Example :- 

my_list =  [11,22,33,44]

print("Before Operation: ", my_list)

my_list.reverse()
print("After Operation: ", my_list) #output = [44,33,22,11]
# _______________________________________________________________________________

'''clear():-The clear( ) method removes all elements from a list'''


# Example :-

my_list = [11,22,33,44]

print("Before Operation: ", my_list)

my_list.clear()
print("After Operation: ", my_list) #Output = [ ]
# _______________________________________________________________________________
 
'''sort():-by default it arranges elements in ascending order. '''

'''sort(reverse = True) => it arranges elements in descending order.'''
# Example :- 
		# Ascending order

my_list = [55,44,33,22,11]
print("before operation : ", my_list)
my_list.sort()
print("after operation: ", my_list) #Output = [11,22,33,44,55]

		# Descending order
my_list = [11,22,33,44,55]
print("before operation : ", my_list)
my_list.sort(reverse=True)
print("after operation: ", my_list) #Output = [55,44,33,22,11]
# _______________________________________________________________________________

'''index():-it returns the first occurrence of any element .'''

# Example :- 

#               0  1    2   3
my_list = [22,44,55,66,11,2,66,22,1,99,55,55]

print("Before Operation: ", my_list)

index_of_55 = my_list.index(55)
print("After Operation: ",index_of_55) #Output = 3
# _______________________________________________________________________________

'''count():-The count( ) method count how many times an element appears in a list '''

# Example :- 

my_list = [22,44,55,66,11,2,66,22,1,99,55,55]

print("Before Operation: ", my_list)

count_of_55 = my_list.count(55)
print("After Operation: ",count_of_55)
# _______________________________________________________________________________

'''copy():-The copy( ) method create a copy of a list'''

# Example :-

my_list = [11,22,33,44,55]

print("Before Operation: ", my_list)

new_list= my_list.copy()
print("After Operation: ",new_list) #Output =[11,22,33,44,55]
# ______________________________________________________________________________