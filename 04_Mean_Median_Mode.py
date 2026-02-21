
# Mean:
''' The mean is the average value of all the values in a dataset. '''

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mean = sum(n) / len(n)
print(f"Mean: {mean}")


# Median
''' The Median is the middle value among all the values in sorted order.'''
# There are two different ways of calculating the median value:
''' when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
    when the total number of values is odd:  Median  = {(n+1)/2}th term '''

n = [22, 34, 12, 56, 13, 9, 10]

n.sort()

if len(n) % 2 == 0:
    m1 = n[len(n) // 2 - 1]
    m2 = n[(len(n) // 2)]
    median = (m1 + m2) / 2
else:
    median = n[len(n) // 2]

print(f"Median: {median}")


# Mode
''' Mode is the most frequently occurring value among all the values '''

n = [1, 2, 2, 3, 3, 3, 4]
mode = max(set(n), key = n.count)
print(f"Mode: {mode}")





# OR
''' You can use the statistics module which has built in function: '''

from statistics import mean, median ,mode
n = [20, 30, 40, 50, 50.50, 50, 60, 70.70, 80]

print(f"Mean: {mean(n)}")
print(f"Median: {median(n)}")
print(f"Mode: {mode(n)}")