def printme(str):
    # 打印
    print(str)
    return


printme("hello world")


def changeList(list):
    """修改"""
    list.append(1)
    print(list)
    return


def changeStr(str):
    print(str)
    """修改字符串"""
    str = 'love'
    print('内部的' + str)
    return


myList = [1, 2, 3]
changeList(myList)
print(myList)

oldStr = 'hate'
changeStr(oldStr)
print(oldStr)
