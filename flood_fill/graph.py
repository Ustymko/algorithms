from typing import List
from edge import *
from vertex import *


class Graph:
    def __init__(self, graph_edges: List[Edge], graph_vertexes: List[List[Vertex]]):
        self.graph_edges = graph_edges
        self.graph_vertexes = graph_vertexes

    def repaint_graph(self, start: Vertex, color: str):
        adjacent_edges = []
        for edge in self.graph_edges:
            if (start == edge.vertex_1 or start == edge.vertex_2) and edge.vertex_2.color == edge.vertex_1.color:
                adjacent_edges.append(edge)
        start.color = color
        for edge in adjacent_edges:
            if edge.vertex_1.color == color and edge.vertex_2.color == color:
                break
            if start == edge.vertex_1:
                self.repaint_graph(edge.vertex_2, color)
            elif start == edge.vertex_2:
                self.repaint_graph(edge.vertex_1, color)

    def parse_vertexes_into_str_array(self):
        parsed = []
        for i in range(len(self.graph_vertexes)):
            parsed.append([])
            for j in range(len(self.graph_vertexes[i])):
                parsed[i].append(self.graph_vertexes[i][j].color)
        return parsed
