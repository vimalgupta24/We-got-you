import streamlit as st
import depression
import anxiety
from sidebar import MultiApp 
import home
import test
from styling import footer
app=MultiApp()

app.add_app("Home", home.app)
app.add_app("Depression", depression.app)
app.add_app("Anxiety", anxiety.app)
app.add_app("Click Here For Testing!!", test.app)
footer()
app.run()