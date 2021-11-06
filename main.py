import streamlit as st
from PIL import Image
from depression import *
from anxiety import *
from styling import *
from testdepr import *
from testanx import *
# link = '[GitHub](http://github.com)'
# st.markdown(link, unsafe_allow_html=True)

st.markdown("# Hope You Score Less Than You Expect,Good Luck!")
st.header("------------------")

anx = st.button("Click When You Are Ready To Begin the Test For Anxiety")
depr = st.button("Click When You Are Ready To Begin the Test For Depression")
if(anx):
    anxious()
    anxiety()
if(depr):
    depressed()
    depression()


footer()
