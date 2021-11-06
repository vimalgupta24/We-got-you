import streamlit as st
import depression
import anxiety
from sidebar import MultiApp 
import home

app=MultiApp()

app.add_app("Home", home.app)
app.add_app("depression", depression.app)
app.add_app("anxiety", anxiety.app)
app.run()