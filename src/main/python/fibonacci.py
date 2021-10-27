# The Fibonacci sequence is a common recursion example because of its
# simplicity. The sequence is as follows:
#   1 1 2 3 5 8 13 21 ...
# Put simply, each number in the sequence is the sum of the previous
# two numbers. So 1+1=2; 1+2=3; 2+3=5; and so on. The first two numbers
# are both 1 because there are not two previous numbers to sum. These
# form the "base case" for the sequence.
#
# The method below calculates the nth fibonacci number. (The "nth" number
# in the sequence is the number in position n, not the value itself.) For
# this sample, n is zero-indexed (meaning the first number is in position
# zero, not position one).
def fibonacci(n):
    # Handle the base case first because it is simplest and requires no
    # computation. If we are looking for position 0 or 1, yield the value 1.
    if n < 2:
        return 1
    # In every other case, yield the sum of the previous two fibonacci
    # numbers. The fact that we are calling the method from within itself
    # is what makes the method 'recursive'.
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Now we demonstrate the above function. You can change the numbers in the
# range to see more or different example values.
for index in range(0, 10):
    print("Fibonacci number %d has value %d" % (index, fibonacci(index)))
