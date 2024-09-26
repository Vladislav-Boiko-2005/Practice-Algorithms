graph={}
graph["start"]={}
graph["start"]["A"]=5
graph["A"]={}
graph["A"]["B"]=1
graph["A"]["D"]=2
graph["A"]["F"]=3
graph["B"]={}
graph["B"]["C"]=10
graph["C"]={}
graph["C"]["E"]=4
graph["D"]={}
graph["D"]["E"]=11
graph["F"]={}
graph["F"]["G"]=2
graph["G"]={}
graph["G"]["E"]=1
graph["E"]={}
graph["E"]["Q"]=5
graph["Q"]={}


infinity=float("inf")

passed=set()

costs={"A":5,"B":infinity,"D":infinity,"F":infinity,"C":infinity,"E":infinity,"G":infinity,"F":infinity,"Q":infinity}

parents={"A":"start","B":None,"D":None,"F":None,"C":None,"E":None,"G":None,"F":None,"Q":None}

def mincost(costs):
    minh=infinity
    cost_itog=None
    for n in costs:
        if (not (n in passed)) and (costs[n]<minh):
            minh=costs[n]
            cost_itog=n
    return cost_itog


knot=mincost(costs)
while knot:
    for i in graph[knot].keys():
        if (not(i in passed)):
            if (graph[knot][i]+costs[knot]<costs[i]):
                costs[i]=graph[knot][i]+costs[knot]
                parents[i]=knot
    passed.add(knot)
    knot=mincost(costs)


print(costs)
print(parents)

