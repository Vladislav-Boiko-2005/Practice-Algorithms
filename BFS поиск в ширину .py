from collections import deque

def proverca (name): return name=="B"

Hash={}
Hash["A"]="1"
Hash["1"]=["2","3","4"]
Hash["2"]="5"
Hash["3"]="6"
Hash["4"]="B"

def BFS(name):
    passed=[]
    a=deque()
    a+=Hash[name]
    while a:
        print(a)
        elem=a.popleft()
        if not (elem in passed):
            passed.append(elem)
            if proverca(elem):
                return True
            else:
                if elem in Hash:
                    a+=Hash[elem]
    return False

print(BFS("A"))