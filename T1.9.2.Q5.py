# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

def averageOfList (num) :
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t
    avg = sumOfNumbers / len (num)
    return avg





print('The average of List is', averageOfList([19, 21, 46, 11, 18]))