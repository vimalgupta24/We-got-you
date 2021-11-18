import streamlit as st
from home import page
from test import quiz
from anxiety import anx
from depression import dep

st.set_page_config(
    page_title="We Got You",
    page_icon="Images/quiz3.png",
    menu_items={
        'About':"Developed by - https://github.com/vimalgupta24"
    }
)

st.markdown("""
	<style>
	/* This is to hide hamburger menu completely */
	/* #MainMenu {visibility: hidden;} */
	/* This is to hide Streamlit footer */
	footer {visibility: hidden;}
	ul[data-testid=main-menu-list] > li:nth-of-type(4), /* Documentation */
	ul[data-testid=main-menu-list] > li:nth-of-type(5), /* Ask a question */
	ul[data-testid=main-menu-list] > li:nth-of-type(6), /* Report a bug */
	ul[data-testid=main-menu-list] > li:nth-of-type(7), /* Streamlit for Teams */
	ul[data-testid=main-menu-list] > div:nth-of-type(2) /* 2nd divider */
		{display: none; visibility:hidden;}
	</style>
""", unsafe_allow_html=True)

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