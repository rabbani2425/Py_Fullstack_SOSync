'''String Slicing:-'''
# there are two types of slicing 
# 1.Two parameter slicing (Staring Point, Ending Point)
# 2.Three parameter slicing (Staring point , Ending point ,Gap)

# --------------------------------------------------------------------
'''Two parameter slicing (Staring Point, Ending Point)'''

# Note :- 
'''By default the staring point will be always 0
By default the ending point will be always Excluded
By default the ending point will be always Last Index'''
# ----------------------------------------------------------------------
# Example 1:-

# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10 --> Indexing

my_string = "Programmaing"

print(my_string)

print(my_string[0:7])

# Explanation:-

# => Staring point = 0 
# => Ending point = 8 (Excluded) 
# => So final range 0 to 7
# => Final output = Program
# -----------------------------------------------------------------
# Example 2:-
my_string = "Programmaing"

print(my_string)

print(my_string[ : 9])

# Explanation:-

# => Staring point = 0
# => Ending point = 9 (Excluded) 
# => So final range 0 indxe to 8
# => Final output = Programma
# ---------------------------------------------------------------------------------
# Example 3:-
my_string = "Programmaing"

print(my_string)

print(my_string[2 : ])

# Explanation:-

# => Staring point = 2
# => Ending point = last index 
# => So final range 0 indxe to last index
# => Final output = ogrammaing
# -----------------------------------------------------------------
# Example 4:-
my_string = "Programmaing"

print(my_string)

print(my_string[ : ])

# Explanation:-

# => by default Staring point = 0
# => By default Ending point = last index 
# => So final range 0 indxe to last index
# => Final output = Programmaing
# ---------------------------------------------------------------------

'''Three parameter slicing (Staring Point, Ending Point, Gap )'''
# Note:-
'''==> First Parametere = Starting Point 
==> Second Parameter = Ending Point 
==> Third parameter = Gap(N - 1)
==> By default gap = 1'''
# ---------------------------------------------------------------------
# Example 1:-

# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10 --> Indexing

my_string = "Programmaing"

print(my_string)

print(my_string[0:7])

print(my_string[0:7:1])

# Exaplanation:-
# ==> starting point = 0 
# ==> Ending point = 7 (Excluded) 
# ==> Gap = 1 (1-1) = 0

# we have to skip 0 element at each iteation
# Final Output = Program
# --------------------------------------------------------------------------------------------
# Example 2:-

# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10 --> Indexing

my_string = "Programmaing"

print(my_string)

print(my_string[1:12:2])

# Exaplanation:-
# ==> starting point = 0 
# ==> Ending point = 12 (Excluded) 
# ==> Gap = 2 (2-1) = 1

# we have to skip 1 element at each iteation
# Final Output = rgamig
# ----------------------------------------------------------------------------------
'''Reverse Indxing '''
#   P   r  o  g  r  a  m  m  i  n  g
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 --> Indexing

print(my_string[: : -1])

# Exaplanation:-
# ==> starting point = 0 
# ==> Ending point = last Index 
# ==> Gap = -1 reverse
# Final Output = gniammargorP
