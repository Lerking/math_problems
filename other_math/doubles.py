'''
I found this problem on the youtube channel MindYouDecisions
Which number doubles when its last digit becodes its first digit???
'''

# We dont need to look at 1 digit numbers
numbers = [*range(100000000000000000, 1000000000000000000)]

num = [x for x in numbers if int(str(x)[1:] + str(x)[:1])/2 == x]
print(num)