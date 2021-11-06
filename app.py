import streamlit as st
from depression import *
from anxiety import *
from sidebar import MultiApp 
from main import *

app=MultiApp()

app.add_app("Home Page", mainfunc.app)
app.add_app("depression", depression.app)
app.add_app("anxiety", anxiety.app)
app.run()