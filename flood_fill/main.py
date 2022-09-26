from graph import *
from input_output_data import *

start_point = Vertex('empty')
width, height, start_i, start_j, color_to_repaint, field = unpack()

color_to_be_repainted = field[start_i][start_j]
edges: List[Edge] = []
vertexes: List[List[Vertex]] = []
# Creating 2d array of vertexes
for i in range(height):
    vertexes.append([])
    for j in range(width):
        vertexes[i].append(Vertex(field[i][j]))

# Creating array of edges
for i in range(height):

    if i == height - 1:
        for j in range(width - 1):
            if vertexes[i][j].color == color_to_be_repainted and \
                    vertexes[i][j + 1].color == color_to_be_repainted:
                edges.append(Edge(vertexes[i][j], vertexes[i][j + 1]))
        break
    for j in range(width):
        if vertexes[i][j].color == color_to_be_repainted:
            if j == width - 1:
                if vertexes[i + 1][j].color == color_to_be_repainted:
                    edges.append(Edge(vertexes[i][j], vertexes[i + 1][j]))
                    break
            if vertexes[i + 1][j].color == color_to_be_repainted:
                edges.append(Edge(vertexes[i][j], vertexes[i + 1][j]))
            if vertexes[i][j + 1].color == color_to_be_repainted:
                edges.append(Edge(vertexes[i][j], vertexes[i][j + 1]))

start_point: Vertex = vertexes[start_i][start_j]
graph_1 = Graph(edges, vertexes)
graph_1.repaint_graph(start_point, color_to_repaint)
output(graph_1.parse_vertexes_into_str_array())
