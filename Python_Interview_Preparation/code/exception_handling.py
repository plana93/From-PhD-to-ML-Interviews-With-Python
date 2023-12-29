# Exception Handling Example
print("### Exception Handling Example ###")

try:
    # Code that might raise an exception
    result = 10 / 0

except ZeroDivisionError:
    # Handling a specific exception
    print("Cannot divide by zero!")

except Exception as e:
    # Handling other exceptions
    print(f"An error occurred: {e}")

finally:
    # Cleanup or final operations
    print("This code always runs, regardless of exceptions.")


print()
print("############################################################")
print()
############################################################
############################################################