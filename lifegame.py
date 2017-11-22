import random as rd
import os
import time


def whatnum(n):#use random number to sim. the lifegame
    if int(n * 10) % 2 == 0:
        return '*'
    else:
        return ' '


def check(amap):
    temp = [[] for i in range(0, 45)]  # python的二维列表真是奇怪
    for x in range(0, 45):
        temp[x] = [0 for i in range(0, 45)]
    for x in range(1, 44):
        for y in range(1, 44):
            kl = [amap[x - 1][y - 1], amap[x - 1][y], amap[x - 1][y + 1]]
            km = [amap[x][y - 1], amap[x][y + 1]]
            kr = [amap[x + 1][y - 1], amap[x + 1][y], amap[x + 1][y + 1]]
            k = kl + km + kr
            for z in k:
                if z == '*':
                    temp[x][y] = temp[x][y] + 1
    for x in range(1, 44):
        for y in range(1, 44):
            if temp[x][y] < 2:
                amap[x][y] = ' '
            if temp[x][y] == 3:
                amap[x][y] = '*'
            if temp[x][y] > 3:
                amap[x][y] = ' '
    return amap


def printarr(amap):
    for x in range(1, 44):
        #time.sleep(0.01)
        print(' '.join(amap[x]))


def flag(condition, amap):
    if condition == 'y':
        print('Please input the round number')
        allround = int(input())
        os.system('cls')
        for x in range(0, allround):
            time.sleep(0.2)
            os.system('cls')
            amap = check(amap)
            printarr(amap)
        print('if you want to contuine please press y')
        print('or you want to quit please press q')
        return flag(input(), amap)
    else:
        os.system('cls')
        return print('Game Finish')


def demo(amap):
    print('Please input the demo number 1 or 2')
    n = int(input())
    if n == 1:
        amap[9][12]  = '*'
        amap[10][12] = '*'
        amap[10][14] = '*'
        amap[11][10] = '*'
        amap[12][15] = '*'
        amap[12][16] = '*'
        amap[13][9]  = '*'
        amap[13][10] = '*'
        amap[14][15] = '*'
        amap[15][11] = '*'
        amap[15][11] = '*'
        amap[15][13] = '*'
        amap[16][13] = '*'
        printarr(amap)
    if n == 2:
        amap[9][10]  = '*'
        amap[10][10] = '*'
        amap[11][9]  = '*'
        amap[11][10] = '*'
        amap[11][11] = '*'
        amap[14][9]  = '*'
        amap[14][10] = '*'
        amap[14][11] = '*'
        amap[15][10] = '*'
        amap[16][10] = '*'
        amap[17][10] = '*'
        amap[18][10] = '*'
        amap[19][9]  = '*'
        amap[19][10] = '*'
        amap[19][11] = '*'
        amap[22][9]  = '*'
        amap[22][10] = '*'
        amap[22][11] = '*'
        amap[23][10] = '*'
        amap[24][10] = '*'
        printarr(amap)
    return amap


def arrinput(amap):
    print('Please input your demo by type space and *')
    print('If you want to stop input one line please press x')
    print('If you want to stop all input please input q')
    print('Now wait for 3s to remember the rules!')
    time.sleep(3)
    os.system('cls')
    for i in range(0, 45):
        temp = list(input())
        for j in range(0, 45):
            if temp[j] == 'x':
                break
            elif temp[j] == 'q':
                return amap
            else:
                amap[i][j] = temp[j]
    return amap


os.system('cls')
print('                  Life Game                    ')
print('           Powered by ViewV @ zxn          \n\n')
print('If you want to start this game please press y\n')
print('If you want to watch two demos please press d\n')
print('If you want to creat your demo please press c\n')
print('      If you want to quit please press q     \n')
foo = input('Now please input :')
if foo == 'd':
    amap = [[] for x in range(0, 45)]
    for x in range(0, 45):
        amap[x] = [' ' for i in range(0, 45)]
    amap = demo(amap)
    flag('y', amap)
if foo == 'q':
    os.system('cls')
    print('Game Finish')
if foo == 'y':
    amap = [[] for x in range(0, 45)]
    for x in range(0, 45):
        amap[x] = [whatnum(rd.random()) for i in range(0, 45)]
    flag('y', amap)
if foo == 'c':
    amap = [[] for x in range(0, 45)]
    for x in range(0, 45):
        amap[x] = [' ' for i in range(0, 45)]
    amap = arrinput(amap)
    flag('y', amap)
