# Recursion
# --------------------------------------------------------------------------------------------------

# rSigma
# --------------------------------------------------------------------------------------------------
# Write a recursive function that, given a number, returns the sum of integers from one up to that number. For example:
# rSigma(5) = 1+2+3+4+5 = 15
# rSigma(2.5) = 1+2 = 3
# rSigma(-1) = 0.

# rFactorial
# --------------------------------------------------------------------------------------------------
# Given a number, return the product of integers from 1 upward to that number. If less than zero, treat as
# zero. If not an integer, treat as an integer. Mathematicians tell us that 0! is equal to 1, so make
# rFact(0) = 1. Examples: 
# rFact(3) = 6 (1*2*3)
# rFact(6.5) = 720 (1*2*3*4*5*6)

# rBinarySearch
# --------------------------------------------------------------------------------------------------
# Write a recursive function that, given a sorted array and a value, determines whether the value is found within the array. For example,
# rBinarySearch([1,3,5,6], 4) = false
# rBinarySearch([4,5,6,8,12], 5) = true





def sayHi():
    for x in range(6):
        print(f'Hi: {x}')

sayHi()


def rSayHi(x = 0):
    if x > 5:
        return
    print(f'recurseive sayHi: {x}')
    x += 1
    rSayHi(x)


rSayHi()


























