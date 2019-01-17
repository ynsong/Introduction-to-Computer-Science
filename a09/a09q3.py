##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 09, Problem 3
##==============================================================================

import check

## constants for examples and tests

G1={1:[2,5],
    2:[1,3],
    5:[4]}
G2={1:[2,4],
    2:[3,4],
    3:[5],
    5:[2,6]}
G3={1:[2,5],
    2:[3],
    5:[4]}
G4={1:[2,3,4],
    2:[3],
    3:[5],
    4:[1,5],
    5:[6]}

## a)
## count_vertices(G) produces the number of vertices in a directed graph G
## count_vertices: (dicof (anyof Int Str) (listof (anyof Int Str))) -> Nat 
## Exampples:
## count_vertices(G1) => 5
## count_vertices(G2) => 6

def count_vertices(G):
    v = []
    for i in G:
        for n in G[i]:
            if i not in v:
                v.append(i)
            if n not in v:
                v.append(n)
    return len(v)

## Testing for count_vertices(G):
check.expect("Q3T1", count_vertices({}), 0)  
check.expect("Q3T2", count_vertices(G1), 5)
check.expect("Q3T3", count_vertices(G2), 6)  
check.expect("Q3T4", count_vertices(G3), 5)  
check.expect("Q3T5", count_vertices(G4), 6)  


## b)
## count_edges(G) produces the number of edges in a directed graph G
## count_edges: (dicof (anyof Int Str) (listof (anyof Int Str))) -> Nat
## Examples:
## count_edges(G1) => 5
## count_edges(G2) => 7

def count_edges(G):
    num = 0
    for i in G:
        num += len(G[i])
    return num

## Testing for count_edges(G):
check.expect("Q3T1", count_edges({}), 0)  
check.expect("Q3T2", count_edges(G1), 5)
check.expect("Q3T3", count_edges(G2), 7)  
check.expect("Q3T4", count_edges(G3), 4)  
check.expect("Q3T5", count_edges(G4), 8)  
        

## c)
## iscycle(G) produces True if there is a cycle in a directed graph G, otherwise 
##  produces False
## iscycle: (dicof (anyof Int Str) (listof (anyof Int Str))) -> Bool
## Examples:
## iscycle(G2) => True
## iscycle({1:[2,5], 2:[3], 5:[4]}) => False

def iscycle(G):
    connected = {}
    for v in G:
        connected[v] = []
        for i in G[v]:
            connected[v].append(i)        
        for n in connected:
            if v in connected[n]:
                for i in G[v]:
                    connected[n].append(i)
        
    for n in connected:
        if n in connected[n]:
            return True
    return False
   
## Testing for iscycle(G):
check.expect("Q3T1", iscycle({}), False)  
check.expect("Q3T2", iscycle(G1), True)
check.expect("Q3T3", iscycle(G2), True)  
check.expect("Q3T4", iscycle(G3), False)  
check.expect("Q3T5", iscycle(G4), True)  
           
        
## d)
## reversed_graph(G) produces a directed grapg that has the same vertices with 
##  consumed directed graph G but reversed edges
## reversed_graph: (dicof (anyof Int Str) (listof (anyof Int Str))) ->
##  (dicof (anyof Int Str) (listof (anyof Int Str)))
## Examples:
## reversed_graph(G1) => {2: [1], 5: [1], 1: [2], 3: [2], 4: [5]}
## reversed_graph(G2) => {2: [1, 5], 4: [1, 2], 3: [2], 5: [3], 6: [5]}
## reversed_graph({1:[2,3,4], 2:[3], 3:[5], 4:[1,5], 5:[6]}) => \
##  {2: [1], 3: [1, 2], 4: [1], 5: [3, 4], 1: [4], 6: [5]}

def reversed_graph(G):
    new_graph = {}
    for i in G:
        for n in G[i]:
            if n not in new_graph:
                new_graph[n] = [i]
            else:
                new_graph[n].append(i)
    return new_graph

## Testing for reversed_graph(G):
check.expect("Q3T1", reversed_graph({}), {})  
check.expect("Q3T2", reversed_graph(G1), {2: [1], 5: [1], 1: [2], 3: [2], 4: [5]})
check.expect("Q3T3", reversed_graph(G2), {2: [1, 5], 4: [1, 2], 3: [2], 5: [3], 6: [5]})  
check.expect("Q3T4", reversed_graph(G3), {2: [1], 3: [2], 4: [5], 5: [1]})  
check.expect("Q3T5", reversed_graph(G4),  {1: [4], 2: [1], 3: [1, 2], 4: [1], 5: [3, 4], 6: [5]}) 
check.expect("Q3T5", reversed_graph({1:[2,3,4], 2:[3], 3:[5], 4:[1,5], 5:[6]}),\
             {2: [1], 3: [1, 2], 4: [1], 5: [3, 4], 1: [4], 6: [5]})

