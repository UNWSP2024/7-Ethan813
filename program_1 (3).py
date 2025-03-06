# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def rainfall():
    RainList = []
    for number in range(12):
        RainList.append(float(input('please enter the amount of rainfall for each month one at a time: ')))
        avg = sum(RainList)
    print('the minimum amount of rain in a month was:', min(RainList))
    print('the maximum amount of rain in a month was:', max(RainList))
    print('the average amount of rain in a month was:', avg/len(RainList))
rainfall()
#ethan collins 3/4/2025 rain calculator