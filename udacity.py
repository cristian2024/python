def find_eulerian_tour(graph):
    tour=[]
    find_tour(graph[0][0],graph,tour)
    return tour
def find_tour(u,E,tour): 
  for (a,b) in E:
    if a==u:
        E.remove((a,b))
        find_tour(b,E,tour)
    elif b==u:
        E.remove((a,b))
        find_tour(a,E,tour)
  tour.insert(0,u)
print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))
