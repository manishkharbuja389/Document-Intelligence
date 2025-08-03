# streamlit_app.py
import streamlit as st
import requests
from pyvis.network import Network
import streamlit.components.v1 as components

API_URL = "http://api:8000"

st.title("Document Intelligence Dashboard")

# Semantic Search
st.header("1. Semantic Search")
query = st.text_input("Enter your query:")
if st.button("Search Semantic"):
    if query:
        res = requests.get(f"{API_URL}/queries/semantic", params={"q": query})
        st.write(res.json())

# Indicator Lookup
st.header("2. Indicator Lookup")
campaign = st.text_input("Campaign Name:")
ind_type = st.selectbox("Indicator Type", ["domains", "urls", "ips", "emails", "socials", "tracking_ids"], index=0)
if st.button("Lookup Indicators"):
    if campaign:
        res = requests.get(f"{API_URL}/queries/indicator_lookup", params={"campaign": campaign, "type": ind_type})
        st.write(res.json())

# Graph Traversal
st.header("3. Graph Traversal")
indicator = st.text_input("Indicator for traversal:")
hops = st.slider("Number of hops", 1, 3, 2)
if st.button("Show Graph"):
    if indicator:
        res = requests.get(f"{API_URL}/queries/graph_traversal", params={"indicator": indicator, "hops": hops})
        data = res.json()
        net = Network(height="500px", width="100%")

        # Simulated nodes and edges, replace with real data
        net.add_node(indicator, label=indicator, color='red')
        for related in data.get("related_indicators", []):
            net.add_node(related)
            net.add_edge(indicator, related)

        net.save_graph("graph.html")
        HtmlFile = open("graph.html", 'r', encoding='utf-8')
        components.html(HtmlFile.read(), height=550)

# Pattern Detection
st.header("4. Pattern Detection")
if st.button("Detect Patterns"):
    res = requests.get(f"{API_URL}/queries/pattern_detection")
    st.write(res.json())

# Campaign Analysis
st.header("5. Campaign Analysis")
if st.button("Analyze Campaigns"):
    res = requests.get(f"{API_URL}/queries/campaign_analysis")
    st.write(res.json())

# Timeline Query
st.header("6. Timeline Query")
indicator_timeline = st.text_input("Indicator for timeline:")
if st.button("Show Timeline"):
    if indicator_timeline:
        res = requests.get(f"{API_URL}/queries/timeline_query", params={"indicator": indicator_timeline})
        st.write(res.json())
