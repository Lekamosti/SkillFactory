import numpy as np

def gues_num(number):
    count = 1
    predict = 50
    l = 25
    while number != predict:
        #print(count, predict)
        count+=1
        if number > predict: 
            predict += l
        elif number < predict: 
            predict -= l
        l = (l+1)//2
    return count  # выход из цикла, если угадали




