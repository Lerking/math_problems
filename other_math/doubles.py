'''
I found this problem on the youtube channel MindYouDecisions
Which number doubles when its last digit becodes its first digit???
'''

# We dont need to look at 1 digit numbers
numbers = [*range(10, 1000000)]

num = [num for num in numbers if int(str(num)[1:] + str(num)[:1])/2 == num]
print(num)