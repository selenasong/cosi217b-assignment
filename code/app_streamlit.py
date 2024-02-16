from collections import Counter
from operator import itemgetter

import streamlit as st
import pandas as pd
import altair as alt
import graphviz

import ner


example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

# example = ("Sebastian Thrun worked at Google in 2007.")

st.set_page_config(layout='wide')

# Create a sidebar with radio buttons
st.sidebar.title("Settings")
selected_option = st.sidebar.radio(
    "Select view",
    ("entities", "dependencies")
)

# Display content based on the selected option
if selected_option == "entities":
    st.markdown('## spaCy Named Entity Recognition')
    text = st.text_area('Text to process', value=example, height=100)
    doc = ner.SpacyDocument(text)
    st.info(text)
    entities = doc.get_entities()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))
    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]})
    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')
    st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
            f'Total number of types: {len(counter)}', unsafe_allow_html=True)
    st.table(entities)
    st.altair_chart(bar_chart)

elif selected_option == "dependencies":
    st.markdown('## spaCy visualization')
    text = st.text_area('Text to process', value=example, height=100)
    doc = ner.SpacyDocument(text)
    st.info(text)
    tab1, tab2 = st.tabs(["table", "graph"])
    parses = doc.get_dependency_parse()
    with tab1:
        df = pd.DataFrame({"head": [p[2]for p in parses], "dependency": [p[1]for p in parses], "token": [p[0]for p in parses]})
        st.table(df)
    with tab2:
        graph = graphviz.Digraph()
        for parse in parses:
                graph.edge(parse[2], parse[0], label=parse[1])

        st.graphviz_chart(graph)