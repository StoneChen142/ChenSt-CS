graph = {'pm':{'d0':82,'d1':81},'sh':{'c3':28,'c4':27},'a0':{'a1':89,'a6':70},'a1':{'a0':89,'a2':110, 'a7':70},'a2':{'a1':110,'a9':70},'a3':{'a4':110,'b0':70}, 'a4':{'a3':110,'a5':88, 'b2':70},'a5':{'a4':88,'b3':70}, 'a6':{'a0':70,'a7':89, 'b4':51}, 'a7':{'a6':89,'a1':70, 'a8':55, 'b5':51}, 'a8':{'a7':55,'a9':55, 'b6':51}, 'a9':{'a8':55,'a2':70, 'b0':54}, 'b0':{'a9':54,'a3':70, 'b1':53}, 'b1':{'b0':53,'b2':57, 'b9':51}, 'b2':{'b1':57,'a4':70, 'b3':88, 'c0':51},'b3':{'b2':88,'a5':70, 'c1': 51},'b4':{'a6':51,'b5':89},'b5':{'b4':89,'c6':107, 'a7': 51},'b6':{'a8':51,'b7':54},'b7':{'b6':54,'c3':54},'b8':{'b9':53,'c4':54},'b9':{'b1':51,'b8':53},'c0':{'b2':51,'c1':88, 'c9': 107},'c1':{'c0':88,'b3':51},'c2':{'c3':54,'c7':53},'c3':{'c2':54,'c4':55, 'b7': 54, 'sh':28}, 'c4':{'c3':55,'c5':54, 'b8': 54,'sh':27},'c5':{'c4':54,'c8':53},'c6':{'c7':55,'b5':107, 'd3': 104}, 'c7':{'c2':53,'c6':55, 'd0': 52}, 'c8':{'c5':53,'c9':56, 'd1': 52},'c9':{'c8':56,'c0':107, 'd8': 104},'d0':{'c7':52,'d4':52, 'd1': 163, 'pm':82},'d1':{'c8':52,'d7':52, 'd0': 163,'pm':81},'d2':{'d3':89,'e0':52},'d3':{'d2':89,'c6':104, 'd4': 55, 'e2':52}, 'd4':{'d3':55,'d0':52, 'd5': 54}, 'd5':{'d4':54,'e4':52},'d6':{'e5':52,'d7':53},'d7':{'d6':53,'d1':52, 'd8': 56}, 'd8':{'d7':56,'c9':104, 'd9': 88,'e7':52}, 'd9':{'d8':88,'e9':52}, 'e0':{'d2':52,'e1':35}, 'e1':{'e0':35,'f1':53}, 'e2':{'d3':52,'e3':55, 'f2': 53},'e3':{'e2':55,'f3':53, 'e4': 54},'e4':{'e3':54,'d5':52, 'e5': 56}, 'e5':{'e4':56,'d6':52, 'e6': 52},'e6':{'e5':52,'f6':53, 'e7': 57},'e7':{'e6':57,'d8':52, 'f7': 53}, 'e8':{'e9':35,'f8':53},'e9':{'e8':35,'d9':52}, 'f0':{'f1':35,'g0':53}, 'f1':{'f0':35,'e1':53, 'f2': 54}, 'f2':{'f1':54,'e2':53}, 'f3':{'f4':53,'e3':53}, 'f4':{'f3':53,'g1':53}, 'f5':{'f6':52,'g2':53}, 'f6':{'f5':52,'e6':53}, 'f7':{'e7':53,'f8':53}, 'f8':{'f7':53,'e8':53, 'f9': 35}, 'f9':{'f8':35,'g3':53}, 'g0':{'f0':53,'g1':197}, 'g1':{'g0':197,'g2':57, 'f4':53}, 'g2':{'g1':57,'g3':197, 'f5':53},'g3':{'g2':197,'f9':53}}

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
            #endif
        #endfor

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
            #endif
        unseenNodes.pop(minNode)

    #endwhile

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    #endwhile
    if shortest_distance[goal] != infinity:
        print('Shortest distance' + str(shortest_distance[goal]))
        print('And the path is' + str(path))
    #endif

#endprocedure

dijkstra(graph,'pm','d0')
