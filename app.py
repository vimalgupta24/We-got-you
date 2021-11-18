import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgbxz
import home
import test

class MultiApp :
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.title("What to do :)")
        # app = st.sidebar.radio(
        app = st.sidebar.selectbox(
            'Choose the app mode-',
            self.apps,
            format_func=lambda app: app['title'])
        app['function']()



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

app=MultiApp()

app.add_app("Home", home.app)
app.add_app("Depression", home.dep)
app.add_app("Anxiety", home.anx)
app.add_app("Click Here For Testing!!", test.app)
footer()
app.run()