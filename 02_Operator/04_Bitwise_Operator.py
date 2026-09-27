"Bitwise operator:"

# binary number

# 0000 = 0
# 0001 = 1
# 0010 = 2
# 0011 = 3 
# 0100 = 4
# 0101 = 5
# 0110 = 6
# 0111 = 7
# 1000 = 8
# 1001 = 9
# 1010 = 10 = A
# 1011 = 11 = B
# 1100 = 12 = C
# 1101 = 13 = D
# 1110 = 14 = E
# 1111 = 15 = F

# NOTE = True --> 1
#      = Flase --> 0


# Rules :-

"Bitwise (&):- if both cases are 1 it gives 1 other wise 0"

"Bitwise (|):- if both cases are 0 it gives 0 other wise 1"

# Example 1 

a = 10  

b = 3 

print(a & b )

# Binary Calculation  

#   1 0 1 0 --> binary of = 10 
# & 0 0 1 1 -->  binary of = 3
#  ---------
#   0 0 1 0 --> Binary of =  2

# --------------------------------------------------------------------------------

# Example 2 

a = 14  
b = 11  

print(a & b)

#   1  1  1  0 --> binary number of 14 → 1110 
# & 1  0  1  1 --> binary number of 11 → 1011
# ---------------
#   1  0  1  0  -->   binary number of 10

# -----------------------------------------------------------------------

# Example 3 

a = 14  
b = 11

print(a | b)

#    1  1  1  0 --> binary number of 14 → 1110 
# |  1  0  1  1 --> binary number of 11 → 1011
# ----------------
#    1  1  1  1  => binary number of 15
