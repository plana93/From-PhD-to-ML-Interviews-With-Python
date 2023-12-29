# Example to Explain Shallow and Deep Copy
print("### Example to Explain Shallow and Deep Copy ###")
import copy

# Original List with nested list
original_list = [1, [2, 3], [4, 5]]

# Shallow Copy
shallow_copy = copy.copy(original_list)

# Deep Copy
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[1][0] = 'X'

# Output
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

print()
print("############################################################")
print()
############################################################
############################################################


