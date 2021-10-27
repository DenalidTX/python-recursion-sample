# The factorial sequence is a common recursion example because it uses a
# very simple formula: To get the factorial value of a number, we multiply
# each number from 1 through the input number and yield the result. So:
#   1! = 1
#   2! = 1*2=2
#   3! = 1*2*3=6
#   4! = 1*2*3*4=6
#
# This sequence has the interesting property that:
#   n! = n * (n-1)!
# We can use that property to simplify the function, as shown in the
# 'else' case.
def factorial(n):
    # Handle the base case first because it is simplest and requires no
    # computation. Both 0 and 1 yield 1. (Assume no negative inputs.)
    if n < 2:
        return 1
    # In every other case, yield the product of n and (n-1)!
    # The fact that we are calling the method from within itself is what
    # makes the method 'recursive'.
    else:
        return n * factorial(n-1)


# Now we demonstrate the above function. You can change the numbers in the
# range to see more or different example values.
for index in range(0, 10):
    print("Factorial number %d has value %d" % (index, factorial(index)))
