import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = {}

def f(string):
    global flag
    current_node = root

    for char in string:
        if char not in current_node.children:
            if current_node.data:
                flag = False
            current_node.children[char] = Node()
        current_node = current_node.children[char]
    current_node.data = string

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = []

    for i in range(n):
        num = input().rstrip()
        nums.append(num)

    nums.sort(key=lambda x: len(x))

    root = Node()
    flag = True
    for num in nums:
        f(num)

    if flag:
        print("YES")
    else:
        print("NO")


import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    db = [input().strip() for _ in range(n)]
    db.sort()
    for j in range(n-1):
        if db[j] == db[j+1][:len(db[j])]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(sol())
