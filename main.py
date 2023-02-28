import heapq
from collections import deque
from twoPointers import TwoPointerFactory


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(TwoPointerFactory.Factory.ARRANGE_CHAR.name)

    TwoPointerFactory.Factory.TOTAL_TRAPPED_RAINWATER.value().solve()


def testDS():
    h = []
    heapq.heappush(h, (1, 'Hello'))

    x = heapq.heappop(h)
    print(x, x[0], x[1])

    q = deque()
    q.append((10, 1))
    q.append((20, 'a'))
    q.append((30, 'b'))
    print(q, q.pop())
    print(q, q.popleft())

    s = {('a', 'b', 'c')}
    print(s)
    xs = ['a', 'b']
    s.add(tuple(xs))
    print(s)
    xs = ['a', 'b', 'c']
    s.add(tuple(xs))
    print(list(map(list, s)))
    l = [4,0,5,-5,3,3,0,-4,-5]
    l.sort()
    print(l)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testDS()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
