import streamlit as st
from PIL import Image
# title
st.title("Are you depressed")
# header
st.header("Lets begin...")
st.subheader("Shall we?")
st.text("Lets begin...") 
st.markdown("# what do you know?")
st.success("done")
st.info("info")
st.warning("Warning")
st.error("error")
value=0
# for k in range(10):
#     st.write(k)
st.write("vimal")
agree=st.checkbox("Fuck you!")
if agree:
    value+=1

# radio button
status=st.radio("Select gender:",('Male','Female'))
st.write(status)

# selection box
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", len(hobbies),hobbies)

# button
# text input
name = st.text_input("Enter Your name", "")


s=st.button("click me and she will love you!")
if s:
    st.text("i love you "+name)
    st.success("finally! someone loves you : )")

level = st.slider("Select the level", 1, 5)
st.text('Selected: {}'.format(level))