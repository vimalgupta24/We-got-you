import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """ <style>   </style> """
    styled = styles(
        # left="100",
        # top="0",
        margin="0",
        # padding_left="100"
        
        )
    body = p()
    foot=(
        div(
            style=styled
        )(body)
    )

    for arg in args:
        body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)
def footer():
    myargs = [
        link("https://buymeacoffee.com/wegotyou",
             image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)
