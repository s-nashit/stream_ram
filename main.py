import graphviz
import streamlit as st

a=graphviz.Graph(engine='neato')
a.node('Database')
a.edge('Source','Process')
a.edge('Process','Source')
a.edge('output','Process')
a.edge('datalake', 'datawarehouse')
a.node('Client')
st.graphviz_chart(a)
