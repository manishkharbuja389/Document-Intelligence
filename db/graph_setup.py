from py2neo import Graph, Node, Relationship

graph = Graph("bolt://neo4j:7687", auth=("neo4j", "myStrongPass123"))

def create_indicator_node(indicator_type, value):
    node = Node("Indicator", type=indicator_type, value=value)
    graph.merge(node, "Indicator", "value")
