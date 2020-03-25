#  P17 error handling
# Let it go!
x = 32
y = 0

print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is my cleanup code')
print()
