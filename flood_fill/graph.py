from typing import List
from edge import *
from vertex import *


class Graph:
    def __init__(self, graph_edges, graph_vertexes: List[List[Vertex]]):
        self.graph_edges = graph_edges
        self.graph_vertexes = graph_vertexes

    def repaint_graph(self, start: Vertex, color: str):
        start.color = color
        for vertex in self.graph_edges[start]:
            if vertex.color != color:
                self.repaint_graph(vertex, color)

    def parse_vertexes_into_str_array(self):
        parsed = []
        for i in range(len(self.graph_vertexes)):
            parsed.append([])
            for j in range(len(self.graph_vertexes[i])):
                parsed[i].append(self.graph_vertexes[i][j].color)
        return parsed
