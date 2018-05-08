#sources:
#https://pypi.python.org/pypi/Dijkstar/2.2
#https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
# http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
# https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3

from dijkstar import Graph, find_path

graph = Graph()
graph.add_edge('A', 'B', {'cost' :4})
graph.add_edge('B', 'A', {'cost' :4})
graph.add_edge('A', 'C', {'cost' :3})
graph.add_edge('C', 'A', {'cost' :3})
graph.add_edge('A', 'E', {'cost' :7})
graph.add_edge('E', 'A', {'cost' :7})
graph.add_edge('B', 'C', {'cost' :6})
graph.add_edge('C', 'B', {'cost' :6})
graph.add_edge('B', 'L', {'cost' :5})
graph.add_edge('L', 'B', {'cost' :5})
graph.add_edge('C', 'D', {'cost' :11})
graph.add_edge('D', 'C', {'cost' :11})
graph.add_edge('D', 'F', {'cost' :6})
graph.add_edge('F', 'D', {'cost' :6})
graph.add_edge('D', 'G', {'cost' :10})
graph.add_edge('G', 'D', {'cost' :10})
graph.add_edge('D', 'L', {'cost' :9})
graph.add_edge('L', 'D', {'cost' :9})
graph.add_edge('F', 'L', {'cost' :5})
graph.add_edge('L', 'F', {'cost' :5})
graph.add_edge('E', 'G', {'cost' :5})
graph.add_edge('G', 'E', {'cost' :5})

cost_func = lambda u, v, e, prev_e: e['cost']
#src = input('Select source router (A-L): ')
#dest =  input('Enter destination vertex (A-L): ')
src = 'L'
print('Source: '+src)

dest = 'A'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))

dest = 'B'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'C'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'D'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'E'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'F'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'G'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))


dest = 'L'
print('Destination: '+dest)
print(find_path(graph, src, dest, cost_func=cost_func))
