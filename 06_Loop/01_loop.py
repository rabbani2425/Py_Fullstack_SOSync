''' What is Loop?'''

# It is used to perform any repeated task.

'''Task: Print "ANKIT" 10 times'''
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")
print("Radhe")

# -------------------------------------------------------------------

'''✔ Using Loop:'''

for i in range(10):
    print("Radhe")
# -------------------------------------------------------------------

'''Types of Loop :-'''
# for
# while
# do while (Not supported in Python)

# -------------------------------------------------------------------

for i in range(3):
    print(i)


# i++ => increment operator 
# i-- => Decrement operator 

# NOTE
# Python does not support increment operator or decrement operator
# that's why we have to use like this , i = i + 1 ,   i += 1

'''Loop Execution Steps'''

# Phase1:

# Step 1: initialization  ( int i = 0 ) 
# Step 2: Condition check ( i <= 3 )   , ( 0 <= 3 ) → True 
# Step 3: condition is true , enter in the loop and execute the code print(i) output → 0
# Step 4: Increment or Decrement i ( i++ ) , 0++ => 1 → i becomes 1.
# ______________________________________

# Phase2:

# Step 1: initialization  ( i = 1 ) 
# Step 2: Condition check ( i <= 3 )   , ( 1 <= 3 ) → True 
# Step 3: condition is true , enter in the loop and execute the code print(i) output →1
# Step 4: Increment or Decrement i ( i++ ) , 1++ → 1 → i becomes 2. 
# ______________________________________

# Phase3:

# Step 1: initialization  ( i = 2 ) 
# Step 2: Condition check ( i <= 3 )   , ( 2 <= 3 ) → True 
# Step 3: condition is true , enter in the loop and execute the code print(i) output → 2
# Step 4: Increment or Decrement i ( i++ ) , 2++ => 3 → i becomes 3.

# ______________________________________

# Phase4:

# Step 1: initialization  ( i = 3 ) 
# Step 2: Condition check ( i <= 3 )   , ( 3 <= 3 ) → False 
# Step 3: we have to exit immediately from the loop because the condition is false .

# -------------------------------------------------------------------

for i in range(3,31,3):
                     print(i) #3,6,9,12,15,18,21,24,27,30

# Output → 3,6,9,12,15,18,21,24,27,30
# Starting point → 3
# Ending point → 31 , excluded
# Gap = 3 , (N-1), 3-1 → 2 we have to skip 2 elements at each iteration

# -------------------------------------------------------------------
'''Loop with List'''

my_list = [11,22,33,44]

for i in my_list:
    print(i)


'''Loop with String'''

my_name = "Rohit"

for i in my_name:
    print(i)


# -------------------------------------------------------------------

'''Example Print numbers from 1 to 5'''

for i in range (1,5):
       print(i)







