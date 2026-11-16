'''continue'''
# If the given condition is true, in that case only we skip the current element and move to the next element.
# Example:
for i in range(6):
    if i == 3:
        continue
    print(i)

# Explanation:
# i = 0
# condition => i == 3

# 0 == 3 => False  # 0 
# 1 == 3 => False  # 1
# 2 == 3 => False  # 2 
# 3 == 3 => TRUE   # Continue => (we skip the current element)

# 4,5
# Final Output => 0,1,2,4,5
