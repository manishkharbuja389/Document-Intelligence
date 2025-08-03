# app/db/graph_queries.py
from py2neo import Graph

# Connect using same settings from graph_setup.py
graph = Graph("bolt://neo4j:7687", auth=("neo4j", "myStrongPass123"))

def find_indicators_by_campaign(campaign_name, indicator_type=None):
    query = (
        "MATCH (i:Indicator)-[:PART_OF_CAMPAIGN]->(c:Campaign {name: $campaign_name}) "
        "RETURN i.type AS type, i.value AS value"
    )
    result = graph.run(query, campaign_name=campaign_name).data()
    if indicator_type:
        return [r["value"] for r in result if r["type"] == indicator_type]
    return [r["value"] for r in result]

def traverse_graph(indicator_value, hops=2):
    query = (
        "MATCH (start:Indicator {value: $value}) "
        "CALL apoc.path.subgraphNodes(start, {maxLevel: $hops}) YIELD node "
        "RETURN DISTINCT node.value AS related_value"
    )
    result = graph.run(query, value=indicator_value, hops=hops).data()
    return [r["related_value"] for r in result if r["related_value"] != indicator_value]

def detect_social_clusters(indicator_type="social_media"):
    query = (
        "MATCH (i:Indicator {type: $type})-[:RELATED_TO]-(j:Indicator {type: $type}) "
        "RETURN i.value AS from, j.value AS to"
    )
    result = graph.run(query, type=indicator_type).data()
    clusters = {}
    for r in result:
        clusters.setdefault(r["from"], set()).add(r["to"])
    return [list(cluster) for cluster in clusters.values() if cluster]

def common_indicators_across_campaigns():
    query = (
        "MATCH (i:Indicator)-[:PART_OF_CAMPAIGN]->(c:Campaign) "
        "WITH i.value AS indicator, count(DISTINCT c) AS campaign_count "
        "WHERE campaign_count > 1 "
        "RETURN indicator"
    )
    result = graph.run(query).data()
    return [r["indicator"] for r in result]

def indicator_timeline(indicator_value):
    query = (
        "MATCH (i:Indicator {value: $value})-[r:MENTIONED_IN]->(d:Document) "
        "RETURN d.date AS date, d.title AS title"
    )
    result = graph.run(query, value=indicator_value).data()
    return [{"date": r["date"], "related": r["title"]} for r in result]
