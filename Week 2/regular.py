import re

hand = open('regex_sum_9994.txt')
    
foo = hand.read()

numbers = re.findall('[0-9]+',foo)

numbers = map(int,numbers)

sum_of_number = sum(numbers)

print sum_of_number

