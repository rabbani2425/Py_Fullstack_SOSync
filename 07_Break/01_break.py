'''break'''
# If the given condition is true, in that case we exit from loop immediately.
# Example:
for i in range(6):
    print(i)  # 0,1,2,3,4,5

for i in range(6):
    if i == 3:
        break
    print(i)

# Explanation:
# i = 0

# 0 == 3 => False   # 0
# 1 == 3 => False   # 1
# 2 == 3 => False   # 2
# 3 == 3 => True    # Break


