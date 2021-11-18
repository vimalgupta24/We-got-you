import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgbxz
from home import page
from test import quiz
from anxiety import anx
from depression import dep

st.set_page_config(
    page_title="We Got You",
    page_icon="Images/quiz3.png",
)

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))
def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)
def layout(*args):
    body = p()
    for arg in args:
        body(arg)
    st.markdown(str(body), unsafe_allow_html=True)
def footer():
    myargs = [
        link("https://buymeacoffee.com/wegotyou",
             image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)

footer()
st.sidebar.title("What to do :)")
app=st.sidebar.selectbox("Choose the app mode",
        ["Home", "Depression", "Anxiety","Quiz"])
if app=="Home":
    page()
elif app=="Depression":
    dep()
elif app=="Anxiety":
    anx()
elif app=="Quiz":
    quiz()
