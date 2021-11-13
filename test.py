import streamlit as st
import time
st.title("This Test Isn't Accurate!!")
count = 0

# Name and age
name = st.text_input("Enter Your Name :", placeholder='Enter Your Name Here')
age = st.text_input("Enter Your Age :", placeholder='Enter Your Age Here')

st.subheader(f"Here It Begins! Good Luck {name}")
# options
global opt1,opt2,opt3,opt4
opt1='Not at all'
opt2='Several Days'
opt3='More than Half of the Days'
opt4='Nearly Every Day' 
    
# questions function
def qn(statement,k):
    temp=0
    st.markdown(statement)
    opt_in=st.radio("", (opt1,opt2,opt3,opt4),key=k)
    if opt_in==opt1:
        temp+=0    
    elif opt_in==opt2:
        temp+=3    
    elif opt_in==opt3:
        temp+=6    
    elif opt_in==opt4:
        temp+=10
    return temp
# qns
count+=qn("#### 1. Little interest or pleasure in doing things",1)
count+=qn("#### 2. Feeling down, depressed, or hopeless",2)
count+=qn("#### 3. Trouble falling or staying asleep, or sleeping too much",3)
count+=qn("#### 4. Feeling tired or having little energy ",4)
count+=qn("#### 5. Poor appetite or overeating",5)
count+=qn("#### 6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down",6)
count+=qn("#### 7. Trouble concentrating on things, such as reading the newspaper or watching television",7)
count+=qn("#### 8. Moving or speaking so slowly that other people could have noticed",8)
count+=qn("#### 9. Thoughts that you would be better off dead, or of hurting yourself",9)
count+=qn("#### 10. If you've had any days with issues above, how difficult have these problems made it for you at work, home, school, or with other people?",10)
count+=qn("### 11. are you feeling well?",11)

st.spinner('hello')
if(st.button("Submit")) :
    with st.spinner('Please Wait...'):
        time.sleep(5)
    st.success("Submitted! Please wait... fetching results")