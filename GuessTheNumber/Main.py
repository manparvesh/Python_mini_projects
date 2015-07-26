__author__ = 'Man Parvesh'
import random

#generating a random integer between 0 to 100
n = int(random.randrange(0, 100, 1))

x = int(raw_input("Enter a number between 0 to 100:\n"))

while True:
    if x == n:
        print "You got it! The correct answer is:", n
        break
    elif 0 > x :
        print "You're going out of bounds!"
        x = int(raw_input("Enter a number between 0 to 100:\n"))
    elif x > 100:
        print "You're going out of bounds!"
        x = int(raw_input("Enter a number between 0 to 100:\n"))
    elif x < n:
        print "That is less than our number. Try a larger number"
        x = int(raw_input("Enter a number between 0 to 100:\n"))
    elif x > n:
        print "That is more than our number. Try a smaller number"
        x = int(raw_input("Enter a number between 0 to 100:\n"))