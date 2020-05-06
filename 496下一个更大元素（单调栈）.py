from collections import deque


def myfunc(list1, list2):
    myDict = {}
    myStack = deque()
    answerList = []
    for i in range(len(list2)):
        if len(myStack) == 0:
            myStack.append(list2[i])

        elif list2[i] > myStack[-1]:
            while len(myStack) != 0 and list2[i] > myStack[-1]:
                myDict[myStack.pop()] = list2[i]
            myStack.append(list2[i])
        else:
            myStack.append(list2[i])

    while len(myStack) != 0:
        myDict[myStack.pop()] = -1

    for j in list1:
        answerList.append(myDict[j])

    return answerList
