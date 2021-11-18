import streamlit as st
import time
def quiz():

    st.markdown("# Hope You Score Less Than You Expect,Good Luck!")
    st.header("------------------")
    "\n"
    st.write("Below is a list of few questions designed to help you determine if you might be experiencing depression,anxiety. The questions relate to life experiences common among people who have such mental health problems. Please read each question carefully, and indicate how often you have experienced the same or similar challenges in the past few weeks.")
    # depr = st.button("Test2")
    "\n"
    st.subheader("How Accurate Is It?")
    st.write("This quiz is NOT a diagnostic tool. Mental health disorders can only be diagnosed by a licensed mental health provider or doctor.")
    "\n"
    count = 0

    # Name and age
    def warnyou(que):
        if not que:
            st.warning("Please Input!!")
            st.stop()
        else:
            st.success("Thankyou :)")
    name = st.text_input("Enter Your Name :", placeholder='Enter Your Name Here')
    warnyou(name)
    age = st.text_input("Enter Your Age :", placeholder='Enter Your Age Here')
    warnyou(age)
    
    # options
    global opt1,opt2,opt3,opt4
    opt1='Not at all'
    opt2='Several Days'
    opt3='More than Half of the Days'
    opt4='Nearly Every Day' 
    with st.form("quiz",clear_on_submit=False):
        # questions function
        st.subheader(f"Here It Begins! Good Luck {name}")
        st.image("Images/quiz2.png")
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
        count+=qn("### 12. Not being able to stop or control worrying",12)
        count+=qn("### 13. Being so restless that it is hard to sit still",13)
        count+=qn("### 14. Feeling afraid, as if something awful might happen",14)
        count+=qn("### 15. Do you often feel emptiness,void or like you are lost cause?",15)
        submitted = st.form_submit_button("Submit")
        if(submitted) :
            st.success("Submitted! Please wait... fetching results")
            mybar=st.progress(0)
            for r in range(100):
                time.sleep(0.05)
                mybar.progress(r+1)
            st.header(f"Your Results: {count}/150")
            if(count<=30):
                st.subheader("No Depression/Minor Anxiety")
                "\n"
                st.write(f"Hey {name},Your answers suggest you may not be suffering from depression. Still if you feel something isn’t quite right we recommend you schedule an appointment with your doctor.")
            elif(count<70 and count>30):
                st.subheader("Minor Depression/Moderate Anxiety")
                "\n"
                st.write(f"Hey {name},Your answers suggest you are suffering from moderate anxiety. Consider watchful waiting, and testing again normally within two weeks. We additionally suggest it would be prudent to start a conversation with your doctor.")
            elif(count>=70 and count<120):
                st.subheader("Moderate Depression")
                "\n"
                st.write(f"Hey {name},Your results indicate that you may be experiencing symptoms of moderate depression. Based on your answers, these symptoms seem to be greatly interfering with your relationships and the tasks of everyday life.These results do not mean that you have anxiety/depression disorder, but it may be time to start a conversation with someone you trust to explore what is going on and how things can get better.")

            elif(count>=120 and count<=150):
                st.subheader("Severe Depression/Anxiety")
                "\n"
                st.write(f"Hey {name},Your answers suggest you are suffering from severe depression. It is important that you schedule an appointment with your doctor or a mental health worker now. \n ")
                st.markdown("#### Your responses indicate that you may be at risk of harming yourself or someone else. If you are in need of immediate assistance, please call the National Suicide Prevention Hotline ")
    st.write("&#11088; This screen is not meant to be a formal diagnosis but is a good way to identify if anxiety is possible problem. Having symptoms of anxiety is different than having an anxiety disorder. In addition, symptoms of anxiety can be caused by other mental health conditions, or other health problems, like a thyroid disorder. A trained professional, such as a doctor or a mental health provider, can make this determination.")
    # app()