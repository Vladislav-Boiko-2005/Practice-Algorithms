from collections import deque
knot={}
knot["A"]="1"
knot["1"]=["2","3","4","5"]
knot["2"]="6"
knot["3"]="7"
knot["5"]="B"


def get (name):
    return name=="B"


def bfs(name):
    passed=[]
    a=deque()
    a.append(knot[name])
    while a:
        elem=a.popleft()
        if not (elem in passed):
            passed.append(elem)
            if get(elem):return True
            if elem in knot: a+=knot[elem]
    return False
print(bfs("A"))


'''
# Схема графа
         A
    /   /  \  \
   2  3    4   5
  /  /          \
 6  7            B
'''