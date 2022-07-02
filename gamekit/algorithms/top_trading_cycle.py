# In The Name Of Allah

import random
import networkx as nx

rooms = [i for i in range(0, 10)]
student = [[random.randint(0, 10) for i in range(0, 10)]for j in range(0, 10)]
aGraph = nx.DiGraph()


def main():
    # initializing---------------------------------------
    # For avoid reputation in student list random
    for x in student:
        i = 0
        for y in x:
            if listfind(x, y, i):
                tmp = random.randint(0, 10)
                while listfind(x, tmp, i):
                    tmp = random.randint(0, 10)
                x[i] = tmp
            i += 1
    # initialize of TTC Algorithm 👇👇👇:down👇👇👇👇 we have an allocation
    # data on node is student and node are room

    # --------------------------------------------------------
    # Algorthm------------------------------------------------
    while checkstabelityofallocation():
        pass
    # --------------------------------------------------------
    # Showing Problem-----------------------------------------
    printlist()
    # --------------------------------------------------------


def printlist():
    print(rooms)
    print("--------------------")
    for x in student:
        print(x)
    print("--------------------")


def listfind(inlist, number, index) -> bool:
    """
    :param inlist: input list
    :param number: search number in list
    :param index: search number index
    :return: if True means number found else not found
    """
    i = 0
    for x in inlist:
        if number == x and i != index:
            return True
        i += 1
    return False


def checkstabelityofallocation() -> bool:
    """
    :return: is there any trading? false or true
    """
    pass


if __name__ == '__main__':
    main()
